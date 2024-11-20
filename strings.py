'''
Author:Divya Kuriakose
Date:08-10-2028
Program:StringDemo
version 1.1
'''

first_name=input("Enter your first name")
last_name=input("Enter your last name")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
extracted_first_name=full_name[:length]
print(extracted_first_name)