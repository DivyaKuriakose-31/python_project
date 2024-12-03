'''
Author :Divya Kuriakose
Date:3-12-2024
Program to find the sum of two numbers using recursion
'''

def add_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_numbers(num1+1,num2-1)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
add_numbers(num1,num2)
print(f"The sum of the two numbers {num1} and {num2} is {add_numbers(num1,num2)}")