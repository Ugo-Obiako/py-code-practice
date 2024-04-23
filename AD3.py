# Select the file name and the search term
file_name = input("Enter the file name")
search_text = input("Enter a search term")

# Check the file for the search term line by line
import os
import re

try:
    with open(file_name) as f:
        for line in f:
            match = re.search(search_text, line)
            if match:
                print(search_text, " found")
except FileNotFoundError:
    print(f"Error: {file_name} not found")