# Name: Akshay Rajput
# Id = 20CS069
# Aim : Concating three dict.

d1 = { 1:10 , 2:20 }
d2 = { 3: 30 , 4:40 }
d3 = { 5 : 50 , 6:60 }

print(d1)
print(d2)
print(d3)
print("-----------")

d4 = {**d1,**d2,**d3}

print(d4)