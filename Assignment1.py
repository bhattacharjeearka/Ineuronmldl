# Problem 1
l = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(i)
converted_list = [str(element) for element in l]
joined_string = ",".join(converted_list)
#print(joined_string)

# Problem 2
FirstName = str(input("Enter your first name: "))
LastName = str(input("Enter your last name: "))
#print(FirstName[::-1] + " " + LastName[::-1])

# Problem 3
import math


def volume(r):
    return 4 / 3 * math.pi * r ** 3


#print(volume(4))
