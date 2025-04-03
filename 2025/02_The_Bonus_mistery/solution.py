from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / 'input'



def read_employee_data():
    return pd.read_csv(DATA_DIR / 'employees.txt', sep=',')

def fill_missing_salary(df):
    # print(df.groupby('department'))
    # print(df.groupby('department')['salary'])
    # print(df.groupby('department')['salary'].mean())
    df['salary'] = df.groupby('department')['salary'].transform(lambda x: x.fillna(x.mean()))

def read_rating_data():
    return pd.read_csv(DATA_DIR / 'ratings.txt', sep=',')

def read_bonus_data():
    bonus_df = pd.read_csv(DATA_DIR / 'bonuses.txt', sep=':', names=['rating', 'bonus'])
    bonus_series = bonus_df.set_index('rating')['bonus']
    return bonus_series.to_dict()

def main():
    employee_df = read_employee_data()
    rating_df = read_rating_data()
    fill_missing_salary(employee_df)

    df = pd.merge(employee_df, rating_df, on='name')

    bonus_mapping = read_bonus_data()
    df['bonus_percent'] = df['rating'].map(bonus_mapping)
    df['bonus_value'] = df['salary'] * (df['bonus_percent']/100)
    df["total_salary"] = df["salary"] + df["bonus_value"]

    df = df.rename(columns={
        'name': 'Employee Name',
        'department': 'Department',
        'salary': 'Base Salary',
        'rating': 'Rating',
        'bonus_percent': 'Bonus %',
        'bonus_value': 'Bonus amount',
        'total_salary': 'Total salary with bonus'
    })

    df.to_excel(DATA_DIR.parent / "output" / "calc.xlsx", index=False)


    print(f"{df['Bonus amount'].sum():,.2f}".replace(',', ' '))


if __name__ == '__main__':

    main()