''' Q1. Write a python code for creating a password for E-Aadhar card. The details used are the
first 4 letters of your name, date and month of your birth. The task is to generate a password
with the lambda function and display it.'''

name = input("Input your name (as on your Aadhar)\n")
dob  = input("Please enter your dob in this order : 'ddmmyyyy'\n")

first = lambda name: name[:4]
last = lambda dob: dob[4:]

pw = first(name) + last(dob)

print("Your password is ",pw)
