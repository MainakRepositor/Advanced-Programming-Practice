# Q2. Python program to accept n inputs about Bill id, Customer Id, Customer Name, Billing Date 
# and no. of units and Amount paid consumed by a customer and generate a report of all of them
n = int(input("Enter number of customers "))

f = list(map(str,input("Enter all the bill ids with a space: ").strip().split()))[:n]

a = list(map(int,input("Enter all the customer ids with a space: ").strip().split()))[:n]

b = list(map(str,input("Enter all the names with a space: ").strip().split()))[:n]

c = list(map(str,input("Enter all the date of payment with a space: ").strip().split()))[:n]

d = list(map(int,input("Enter all the units with a space: ").strip().split()))[:n]

e = list(map(float,input("Enter all the amounts paid with a space: ").strip().split()))[:n]

print("\nGenerating Bill Reports.............100%")
print("\n Reports generated\n")

print("Cust_id    Bill_id     Name      LDoP  Units   Bill amt")
for i in range(n):
    if(e[i]>0.0):
        print(f[i],"   ",a[i],"   ",b[i],"  ",c[i],"  ",d[i],"  ",e[i])
