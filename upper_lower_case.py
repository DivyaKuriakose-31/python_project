'''
Author:Divya Kuriakose
Date:31-11-2024
Program to find the number of upper and lower case
'''

def count_upper_case_lower_case_characters(input_string):
    upper_characters_count= 0
    lower_characters_count= 0
    for character in input_string:
        if character.isupper():
            upper_characters_count += 1
        elif character.islower():
            lower_characters_count += 1
    return upper_characters_count,lower_characters_count

input_string=input('Enter a string:')
upper_characters_count, lower_characters_count=count_upper_case_lower_case_characters(input_string)
print("No. of upper case in the string",upper_characters_count)
print("No of lower case in the string",lower_characters_count)




