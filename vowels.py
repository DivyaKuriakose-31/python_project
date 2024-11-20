'''
Author:Divya Kuriakose
Date:29-10-2024
'''

string_input=input("Enter a string")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"The number of given string{string_input}={vowels_count}")