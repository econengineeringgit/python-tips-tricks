from pathlib import Path

import pandas as pd
from faker import Faker

THIS_DIR = Path(__file__).parent

def generate_employees(n: int, fake:Faker):
    employees = []
    for _ in range(n):
        employees.append({
            'name': fake.name(),
            'department': fake.random_element(elements=('General simulations', 'Software support', 'Automotive simulations', 'R&D')),
            'salary': fake.random_int(min=300_000, max=1_300_000, step=10_000),
            'rating': fake.random_int(min=1, max=5),
        })
    df = pd.DataFrame(employees)
    return df

def generate_employees_csv(employee_df: pd.DataFrame):
    df = employee_df[["name", "department", "salary"]].copy()
    random_rows = df.sample(frac=0.05, random_state=42)
    df.loc[random_rows.index, 'salary'] = None
    df["salary"] = df["salary"].astype("Int64")

    df.to_csv(THIS_DIR/'employees.txt', index=False)


def generate_rating_csv(employee_df: pd.DataFrame):
    df = employee_df[["name", "rating"]].copy()
    df.to_csv(THIS_DIR/'ratings.txt', index=False)

if __name__ == '__main__':
    faker = Faker("hu_HU", seed=42)

    employee_df = generate_employees(100, faker)
    generate_employees_csv(employee_df)
    generate_rating_csv(employee_df)