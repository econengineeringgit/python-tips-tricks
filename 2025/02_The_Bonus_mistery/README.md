# The Great Bonus Mystery

It's bonus season at noCe engineering kft., and the HR department is in panic mode! The payroll system malfunctioned and generated incomplete and corrupted reports about employee bonuses. You have been tasked with fixing this mess quickly—otherwise, nobody gets their bonus this year!

---

You have been provided with three files from HR, but unfortunately, there's missing data in one of them:

## Provided Files

- `employees.txt`: Contains employee names, departments and base salaries. Some salaries are missing due to system errors.

```plaintext
Dr. Magyar Tamás,R&D,1140000
Dr. M. Péter Mária,General simulations,1160000
Váradi Szabolcs,Software support,860000
Dr. Juhász Jánosné Horváth Mária,Software support,
```

- `ratings.txt`: Contains employee names and their performance ratings (1-5). Complete data.

```plaintext
Dr. Magyar Tamás,4
Dr. M. Péter Mária,2
Váradi Szabolcs,1
Dr. Juhász Jánosné Horváth Mária,3
```

- `bonuses.txt`: Contains bonus percentages based on ratings.

```plaintext
1:0
2:20
3:40
4:50
5:60
```

## Your task

Write a code that calculates the bonuses for each employee based on their performance **rating** and **base salary**. The bonus should be calculated as a percentage of the base salary according to the rating in `bonuses.txt`.

The salary of an employee with a **missing value** should be considered as the average of the salaries of the employees in the same department.

1. Calculate the sum of bonuses that the company needs to pay.
2. Save the results to an Excel file, so the HR department can easily process the payments.

The output should be written to a new Excel file named `final_bonuses.xlsx` with the following format:

Employee Name | Base Salary | Rating | Bonus % | Bonus Amount | Total Salary with Bonus
--- | --- | --- | --- | --- | ---
Dr. Magyar Tamás   | 1140000       | 4      | 50%     | 570000       | 1710000
Dr. M. Péter Mária | 1160000       | 2      | 20%     | 232000       | 1392000
Váradi Szabolcs    | 860000        | 1      | 0%      | 0            | 860000

---
<details>
  <summary>💡 Hints</summary>

- use the pandas library to read the data from the files and perform the calculations
- you can use the `pd.read_csv()` function to read the data from the files
- you can use the `pd.merge()` function to combine the data from the different files
- you can use the `pd.to_excel()` function to save the results to an Excel file
- make sure to handle missing base salary values by calculating the average salary per department

</details>
