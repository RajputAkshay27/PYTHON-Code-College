# Name: Akshay Rajput
# Id = 20CS069
# Aim : Adding an element to a tuple.

fruits = { "Mango", "Apple" , "Orange"}
Company = {"Microsoft", "Apple" , "Google"}

print(fruits)
print(Company)

print(f"Fruits Intersection Company is {fruits.intersection(Company)}")
print(f"Fruits Union Company is {fruits.union(Company)}")
print(f"Fruits Difference Company is {fruits.difference(Company)}")
print(f"Company Difference Fruits is {Company.difference(fruits)}")