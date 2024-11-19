'''
Author:Divya Kuriakose
Date:19-11-2024
program for pattern printing
'''
#increasing triangle
limit=int(input("Enter a limit"))
for i in range(limit):
    for j in range(i+1):
        print("*",end=" ")
    print()
#decreasing triangle
limit=int(input("Enter a limit:"))
for i in range(limit):
    for j in range(limit-i):
        print("*",end=" ")
    print()
#hill triangle
limit=int(input("Enter the limit:"))
for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(2*i-1):
            print("*",end="")
    print()
#reverse hill triangle
limit=int(input("Enter the limit:"))
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
