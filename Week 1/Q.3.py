#Q3. Prediction of Electric Bill based on previous month units

n = int(input("Enter number of customers "))

f = list(map(str,input("Enter all the bill ids with a space: ").strip().split()))[:n]

a = list(map(str,input("Enter all the names with a space: ").strip().split()))[:n]

b = list(map(int,input("Enter all the month 1 units with a space: ").strip().split()))[:n]

c = list(map(int,input("Enter all the month 2 units with a space: ").strip().split()))[:n]

d = list(map(int,input("Enter all the month 3 units with a space: ").strip().split()))[:n]

print("\nPredicting Result..........100%")
print("Generating Prediction Output\n")

print("Cus_id    Name     Month 1   Month 2   Month 3   Estimated Bill")
t = 0.0
for i in range(n):
    t = (c[i]+d[i]+b[i])/3
    print(f[i],"    ",a[i],"     ",b[i],"     ",c[i],"     ",d[i],"     ",t)
