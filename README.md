# Title: Loan Eligibility Calculator

## Description
This project involves the development of a loan eligibility calculator using Python. The script reads loan data from a CSV file, calculates the loan duration, determines eligibility based on a predefined criterion, and outputs the results in both the console and a CSV file.

## Code Overview
1. **Loan Data Handling:**
   - The Dataset class is responsible for reading loan data from a CSV file using the pandas library.
   - Loan data includes the borrower's name, borrowed amount, interest rate, and monthly payment.

2. **Loan Calculation:**
   - The Calculation class performs loan duration calculations and determines eligibility.
   - The loan duration is calculated using the formula for the time required to pay off a loan with a fixed monthly payment.
   - Eligibility is determined based on a maximum loan duration of 30 years.

3. **Results Presentation:**
   - The CSVWriter class writes the loan results, including loan name, duration, and eligibility, to a CSV file.
   - The Calculation class prints the results to the console, indicating the loan name, duration, and eligibility status.

## Conclusion
This Python script provides a simple yet effective tool for calculating loan durations and determining eligibility based on predefined criteria. It can be easily adapted for different loan scenarios by providing input data in the specified CSV format. The project demonstrates the use of classes and file handling in Python for practical financial calculations.
