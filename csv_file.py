import csv 
with open('students.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'age', 'grade'])
    writer.writerow(['a', 20, 'A'])
    writer.writerow(['b', 21, 'B'])
    writer.writerow(['c', 22, 'C']) 
with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

    