import numpy as np
import pandas as pd

# Read employees data
employees = pd.read_csv(r"d:\MizsakPeti\3_Proj\99_econ_TOOLS\python-tips-tricks\2025\02_The_Bonus_mistery\input\employees.txt")
employees['salary'] = pd.to_numeric(employees['salary'], errors='coerce')

# Fill missing salary with department average
employees['salary'] = employees.groupby('department')['salary'].transform(lambda x: x.fillna(x.mean()))

# Read ratings data (from merged_data.txt, select only name and rating)
ratings = pd.read_csv(r"d:\MizsakPeti\3_Proj\99_econ_TOOLS\python-tips-tricks\2025\02_The_Bonus_mistery\input\ratings.txt")
ratings = ratings[['name', 'rating']]

# Merge employees with ratings on name
df = pd.merge(employees, ratings, on='name', how='inner')

# Read bonus percentages and create a dictionary
bonus_dict = {}
with open(r"d:\MizsakPeti\3_Proj\99_econ_TOOLS\python-tips-tricks\2025\02_The_Bonus_mistery\input\bonuses.txt") as f:
    for line in f:
        parts = line.strip().split(":")
        if len(parts) == 2:
            key, value = parts
            bonus_dict[int(key)] = float(value)

# Calculate bonus and total salary
df['Bonus %'] = df['rating'].map(bonus_dict)
df['Bonus Amount'] = df['salary'] * df['Bonus %'] / 100
df['Total Salary with Bonus'] = df['salary'] + df['Bonus Amount']

# Calculate total bonus sum
total_bonus = df['Bonus Amount'].sum()
print("Total bonus payout:", total_bonus)

# Reorder and rename columns for Excel output
df_final = df[['name', 'salary', 'rating', 'Bonus %', 'Bonus Amount', 'Total Salary with Bonus']]
df_final.columns = ['Employee Name', 'Base Salary', 'Rating', 'Bonus %', 'Bonus Amount', 'Total Salary with Bonus']

# Write result to an Excel file
df_final.to_excel(r"d:\MizsakPeti\3_Proj\99_econ_TOOLS\python-tips-tricks\2025\02_The_Bonus_mistery\output\final_bonuses_copilot.xlsx", index=False)
