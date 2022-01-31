annual_salary=int(input("Enter your annual salary"))
if annual_salary < 150000 :
 print("No Tax")
elif (annual_salary > 150001 and annual_salary <300000):
 print((1/100)*annual_salary,"is your Tax")
elif (annual_salary > 300000 and annual_salary <500000):
 print((2/100)*annual_salary,"is your Tax")
elif annual_salary > 500000:
 print((3/100)*annual_salary,"is your Tax")


 
