'''
Author:Divya Kuriakose
Date:29-10-2024
Program to display a multiplication table
'''

number=int(input("Enter a number"))

for i in range(1,13):
    multiple=number*i
    print(f"{number}*{i}={multiple}")