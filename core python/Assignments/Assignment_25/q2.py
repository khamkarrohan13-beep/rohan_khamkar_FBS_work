# 2. Create a function that extracts all the dates from a given text using regular expressions.
# Dates can be in various formats like MM/DD/YYYY, DD-MM-YYYY, or written out like
# January 1, 2023. Extract all such date occurrences.

import re

def extract_dates(text):
    pattern = r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|[A-Za-z]+ \d{1,2}, \d{4}"
    
    dates = re.findall(pattern, text)
    return dates


text = input("Enter text: ")

print("Dates:", extract_dates(text))