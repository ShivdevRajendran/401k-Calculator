import math

age = int(input("Enter age: "))
retireAge = int(input("Enter planned age of retirement: "))
salary = float(input("Enter current annual salary: "))
salaryIncrease = (float(input("Enter current annual salary increase (percentage value): ")) / 100) + 1
contriPercent = float(input("Enter contribution percent: ")) / 100
balance = float(input("Enter current 401k balance: "))
returnRate = float(input("Enter annual rate of return (percentage value): ")) / 100
returnRateIncrease = (float(input("Enter annual rate of return increase (percentage value): ")) / 100) + 1
employerMatchPercent = float(input("Enter employer match percentage: ")) / 100
employerMatchEnds = float(input("Enter employer match ends (percentage value): ")) / 100

contriTotal = 0
employeeTotal = 0
years = retireAge - age

for i in range(0, years):
    if (i > 0): salary = salary * salaryIncrease
    num = salary * contriPercent
    contriTotal += num
    employerContri = num * employerMatchPercent
    if employerContri > (salary * employerMatchEnds): employerContri = salary * employerMatchEnds
    employeeTotal += employerContri
    balance += employerContri
    balance += (balance * returnRate)
    returnRate *= returnRateIncrease
    print("\n\nYear ", i , " Projections\nProjected salary: ", round(salary, 2), "\nProjected contribution amount: ", round(num, 2), "\nProjected employer contribution: ", round(employerContri, 2))

balance += contriTotal
print("\n---------------------------\n\nTotal employee contributions: " , round(contriTotal, 2), "\nTotal employer contribution: ", round(employeeTotal, 2), "\nTotal 401k balance: ", round(balance, 2))

