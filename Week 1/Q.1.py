# Q1. Python program to accept n inputs about Customer Id, Customer Name, Billing Month 
# and no. of units consumed by a customer and generate a report of all of them
n = int(input("Enter number of customers "))

a = list(map(int,input("\nEnter all the ids with a space: ").strip().split()))[:n]

b = list(map(str,input("Enter all the names with a space: ").strip().split()))[:n]

c = list(map(str,input("Enter all the months with a space: ").strip().split()))[:n]

d = list(map(int,input("Enter all the units with a space: ").strip().split()))[:n]
print("\n Generating report......100%")
print("\n Report generated\n")
print("id     Name      Month     Units     Bill amt")
min_bill = 100
for i in range(n):
    if(d[i]<=200):
        payAmount=d[i]*1.20 + min_bill
        
    elif(d[i]<=400):
        payAmount=(200*1.20)+(d[i]-200)*1.50 + min_bill
        
    elif(d[i]<=600):
        payAmount=(200*1.20)+(400*1.50)+(d[i]-400)*1.80
        payAmount = payAmount * 1.15 + min_bill
    
    else:
        payAmount=(200*1.20)+(400*1.50)+(600*1.80)+(d[i]-600)*2.00
        payAmount = payAmount * 1.15 + min_bill
    
    print(a[i],"   ",b[i],"  ",c[i],"  ",d[i],"  ",payAmount)
    
    
        



