list_1=[]
list_2=[]
list1_size=int(input("Enter the size of list1:"))
print("Enter the elements in list1:")
for i in range(list1_size):
    list_1.append(int(input()))
list2_size=int(input("Enter the size of list2:"))
print("Enter the elements in list2:")
for i in range(list2_size):
    list_2.append(int(input()))
print(list_1,list_2)
list_3=(list_1+list_2)
print(list_3)
even_list=[]
odd_list=[]
for i in list_3:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)
merged_list= (even_list + odd_list)
print(merged_list)
