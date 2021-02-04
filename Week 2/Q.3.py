'''Q3. A web application is developed for a bank. The first page gets the user id and password.
Write a python application to check the credentials of the user. The task is to enter 5 pairs of
user id and password in a dictionary and perform the following.
Credentials: {Ramesh: 12345, Seetha: abcde, Abhishek: pqrst, Ramya: 98765, Priya: xyzab}'''



n = int(input("Enter number of customers "))
a = list(map(str,input("\nEnter all the names with a space: ").strip().split()))[:n]
b = list(map(str,input("\nEnter all the password with a space: ").strip().split()))[:n]

Credentials = dict(zip(a, b))



name = input("\nEnter your name     : ")
pw   = input("Enter your password : ")


if name in Credentials.keys():
    if pw in Credentials.values():
        print("\n\nDear",name,",you are welcome to our bank")
    else:
        print("Your details does not match with our records")
else:
    print("Your details does not match with our records")

