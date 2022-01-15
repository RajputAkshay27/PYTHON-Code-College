# Name: Akshay Rajput
# Id = 20CS069
# Aim : Adding a key to dictonary

d1 = { 0:10 , 1:20}
print(d1)

print("-----------")
key = 0
sum = 0
for i in d1:
    sum += d1[i]
    key += 1

d1[key] = sum

print(d1)