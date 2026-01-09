import pandas as pd
import numpy as np

sheets = pd.ExcelFile("Cfkust_ Data Import Assignment.xlsx").sheet_names
print(sheets)

constituentInput = pd.read_excel("Cfkust_ Data Import Assignment.xlsx", sheet_name="Input Constituents")
print(constituentInput.head())

emailInput = pd.read_excel("Cfkust_ Data Import Assignment.xlsx", sheet_name="Input Emails")
print(emailInput.head())

donationInput = pd.read_excel("Cfkust_ Data Import Assignment.xlsx", sheet_name="Input Donation History")
print(donationInput.head())






