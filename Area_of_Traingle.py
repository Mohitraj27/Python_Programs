a=int(input("Enter the 1st side of a Triangle"))
b=int(input("Enter the 2nd side of a Triangle"))
c=int(input("Enter the 3rd side of a Triangle"))
s=(a+b+c)/2
Area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of a Triangle is ",Area)
