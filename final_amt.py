'''
Author:Divya Kuriakose
Date:15-10-2024
Program to calculate the final amount after applying the discount from an online store
'''

purchase_amount=int(input("Enter total purchase_amount:"))
if purchase_amount>500:
    discount=purchase_amount*0.20
    final_amount=purchase_amount-discount
    print("final amount after applying 20% :",final_amount)
elif  purchase_amount>=200 and purchase_amount<=500:
    discount=purchase_amount*0.10
    final_amount=purchase_amount-discount
    print ("final amount after applying 10% :",final_amount)
else:
    final_amount=purchase_amount
    print("no discount is applied:")