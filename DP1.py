# Name: Akshay Rajput
# Id = 20CS069
# Aim : TO check if a given key is present inside the dictionary 

key = input("Enter key to find: ")
random = {"Akshay" : "CSE" , "Jay" : "ME" ,"Bhargavi" : "CSE" , "Tushar" : "IT"}

print(random)

print("---- ------")

for k in random:
    if k == key:
        print("Key is present in Dictionary")
        exit()

print("Key is not Present in dictonary")