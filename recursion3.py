'''
Author:Divya Kuriakose
Date:3-12-2024
Program to multiply two numbers using recursion
'''

def multiply_numbers(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+ multiply_numbers(num1,num2-1)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
multiply_numbers(num1,num2)
print(f"The product of numbers {num1} and {num2} is {multiply_numbers(num1,num2)}")