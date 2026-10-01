"""
Program:  income tax.py
Author:   Abba Abdullahi Adam
Date:     2026-30-09

Purpose:  Compute the gross income and a number of dependents.
Input:     the gross income and a number of dependents.
Output:   the income tax.
"""

TAX_RATE = 0.2
EXEMPTION_PER_DEPENDENT = 10000
grossIncome = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))
taxableIncome = grossIncome - dependents * EXEMPTION_PER_DEPENDENT
tax = TAX_RATE * taxableIncome
print("The income tax is $" + str(tax))
