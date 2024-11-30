'''Author:Divya Kuriakose
Date:31-11-2024
Program to find whether the triangle is right triangle or not
'''

def is_right_angle_triangle(first_side,second_side,third_side):
    sides=[first_side,second_side,third_side]
    sides.sort()
    if sides[2]**2==sides[0]**2 + sides[1]**2:
        return True
    return False

first_side=int(input("Enter the length of the first side:"))
second_side=int(input("Enter the length of the second_side:"))
third_side=int(input("Enter the length of the third side:"))
if is_right_angle_triangle(first_side,second_side,third_side):
     print("The given triangle is right triangle")
else:
    print("The given triangle is not a right triangle")
