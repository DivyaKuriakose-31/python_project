'''Author:Divya Kuriakose
Date:31-11-2024
program to identify the valid number'''


def mobile_number(phone_num):
    if len(phone_num)==10 and phone_num[0] in "789":
        print("Its a valid phone number")
    else:
        print("Its a invalid phone number ")
phone_num=input("Enter the phone number:")
mobile_number(phone_num)
