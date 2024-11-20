'''
Author:Divya Kuriakose
Date:15-10-2024
program to find the sum of digits
'''

number=int(input("Enter a number:"))
sum=0
while(number>0):
    r=number%10
    number=number//10
    sum=sum+r
print("Sum of digits:",sum)