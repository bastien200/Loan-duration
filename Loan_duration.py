import pandas as pd
import math
import csv

class Dataset():
    def __init__(self, name, amount_borrowed, rate, monthly):
        self.name = name
        self.amount_borrowed = amount_borrowed
        self.rate = rate
        self.monthly = monthly

    @classmethod
    def read_from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='cp1252') as myfile:
                reader = pd.read_csv(myfile, delimiter=';')
                data_list = []
                for index, row in reader.iterrows():
                    data = cls(row['Name'], row['Amount borrowed'], row['Rate'], row['Monthly'])
                    data_list.append(data)
                return data_list
        except FileNotFoundError:
            print(f"Le fichier {file_path} n'a pas été trouvé.")
            return []

class Calculation:
    def __init__(self, data_list):
        self.data_list = data_list

    def calculate_duration(self, amount, rate, payment):
        monthly_rate = rate / 12
        duration = math.log(payment / (payment - monthly_rate * amount)) / math.log(1 + monthly_rate)
        return duration / 12

    def is_eligible_for_loan(self, duration):
        if duration > 30:
            return False
        return True

    def calculate_all_durations(self):
        results = []
        for data in self.data_list:
            amount = float(data.amount_borrowed.replace(' ', '').replace(',', '.'))
            payment = float(data.monthly.replace('-', '').replace(' ', '').replace('€', '').replace(',', '.'))
            rate = float(data.rate.replace(' ', '').replace('%', '').replace(',', '.')) / 100
            duration = self.calculate_duration(amount, rate, payment)
            eligibility = self.is_eligible_for_loan(duration)
            results.append((data.name, duration, eligibility))
        return results

    def print_results(self):
        for result in self.calculate_all_durations():
            name, duration, eligibility = result
            if eligibility:
                print(f"{name}: Durée du prêt: {duration:.2f} ans (Éligible)")
            else:
                print(f"{name}: Durée du prêt: {duration:.2f} ans (Non éligible)")

class CSVWriter:
    def __init__(self, calculation):
        self.calculation = calculation

    def write_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Loan', 'Duration in years', 'Eligibility'])
            for result in self.calculation.calculate_all_durations():
                loan_name, duration, eligibility = result
                duration = int(round(duration))
                writer.writerow([loan_name, duration, eligibility])

file_path = "/Users/bastien/Downloads/customers.csv"
data_list = Dataset.read_from_file(file_path)

#for data in data_list:
    #print(f"Name: {data.name}, Amount Borrowed: {data.amount_borrowed}, Rate: {data.rate}, Monthly: {data.monthly}")

instance = Calculation(data_list)


csv_writer = CSVWriter(instance)
csv_writer.write_csv('/Users/bastien/Downloads/loan_results.csv')


