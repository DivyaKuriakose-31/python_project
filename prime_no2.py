'''
Author:Divya Kuriakose
Date:29-10-2024
program to find prime numbers in a given limit
'''

limit=int(input("Enter a limit"))
for number in range(2,limit+1):
    isprime = True
    for i in range(2,(number//2)+1):
        if number%i==0:
            isprime = False
            break
    if isprime:
        print(number,end=" ")