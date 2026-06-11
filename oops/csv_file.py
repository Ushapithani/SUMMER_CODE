'''import csv 
with open('students.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'age', 'grade'])
    writer.writerow(['a', 20, 'A'])
    writer.writerow(['b', 21, 'B'])
    writer.writerow(['c', 22, 'C']) 
with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)'''


# craete a file employess,csv woth name id aand salary import 10 employees and read the file
#  print all the employee details 
# find hifhest salaryy
# find avg salaray 
# print the count of employee whose salary is greater than avg salary 
import csv 
with open('employees.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'id', 'salary'])
    writer.writerow(['a', 1, 50000])
    writer.writerow(['b', 2, 60000])
    writer.writerow(['c', 3, 55000]) 
    writer.writerow(['d', 4, 70000]) 
    writer.writerow(['e', 5, 65000]) 
    writer.writerow(['f', 6, 80000]) 
    writer.writerow(['g', 7, 75000]) 
    writer.writerow(['h', 8, 90000]) 
    writer.writerow(['i', 9, 85000]) 
    writer.writerow(['j', 1, 95000])
with open('employees.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    employees = []
    for row in reader:
        employees.append({'name': row[0], 'id': row[1], 'salary': row[2]})
        print(row)
# HIGHEST SALARY 
highest_salary = max(employees, key=lambda x: x['salary'])
print(f"Highest Salary: {highest_salary['name']} with salary {highest_salary['salary']}")





    