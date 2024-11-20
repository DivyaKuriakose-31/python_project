'''
Author:Divya Kuriakose
Date:22-10-2024
Program to convert temperature values back and forth between Celsius and Fahrenheit

'''


temperature=int(input("Enter temperature:"))
scale=(input("Is this is (C) or (F)?"))
if(scale=="C"):
   f=(9/5 * temperature)+32
   print(temperature,"Celsius is",f,"Fahrenheit")
else:
    c=5/9 *(temperature-32)
    print(temperature,"Fahrenheit is",c,"Celsius")