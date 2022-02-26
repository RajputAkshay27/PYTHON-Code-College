# student id: 20cs069
# student name : Rajput Akshaykumarsingh virendra
# aim : You are given n words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word

n = int(input())

# list of all the values entered by user
ls = [] 

# list of unique values entered by user in order
temp = []

for i in range(n):
    ls.append(input())
    if temp.count(ls[i]) == 0:      #checking for unique values of string before appending
        temp.append(ls[i])

# Final loop to print answer
for i in temp:
    print(ls.count(i))
            