# Name: Akshay Rajput
# Id = 20CS069
# Aim : Sum of all the items inside Dictionay

d1 = { "A" : 1 , "B" : 2 , "C" : 3}
print(d1)

print("-----------")
sum = 0

for i in d1:
    sum = sum + d1[i]

print(sum)