# student id: 20cs069
# student name : Rajput Akshaykumarsingh virendra
# aim : You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

str = input()

ls = ""         # empty string to store answer
for i in str:
    ls = ls + i.swapcase()  #   swapping case of each letter
print(ls)
