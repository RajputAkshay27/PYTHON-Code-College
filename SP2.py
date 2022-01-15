# Name: Akshay Rajput
# Id = 20CS069
# Aim : Adding an element to a tuple.

fruits = { "Mango", "Apple" , "Orange"}
print(fruits)

var = input("Enter The name of Fruit: ")

for fruit in fruits:
    if fruit == var:
        fruits.remove(var)
        print("element is Deleted")
        exit()

print("No such element is present")