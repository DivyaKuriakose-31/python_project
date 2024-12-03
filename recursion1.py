'''
Author:Divya Kuriakose
Date:3-12-2024
program to find the factorial of a given number
'''

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
factorial(5)
print(factorial(5))
