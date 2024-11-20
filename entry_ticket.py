'''
Author:Divya Kuriakose
Date:15-10-2024
program to determine the entry ticket in a zoo based on age
'''

age=int(input("Enter your age:"))
if(age<10):
    print("Fare is 7")
elif(age>=10 and age<=60):
    print("Fare is 10")
else:
    print("Fare is 5")