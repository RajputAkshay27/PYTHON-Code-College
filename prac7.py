# student id: 20cs069
# student name : Rajput Akshaykumarsingh virendra
# aim : Given a string, find if it is a lapindrome

n = int(input())

# list of all the values entered by user
ls = [] 

for i in range(n):
    ls.append(input())
    
for i in ls:
    if len(i) % 2 == 0:     #if the length of string is even
        p1 = i[0:int(len(i)/2)]     # first len(i)/2 characters are stored in p1
        p2 = i[int(len(i)/2):]      # character from len(i)/2 index to last index are stored in p2
    else:
        p1 = i[0:int(len(i)/2)]     # first len(i)/2 characters are stored in p1
        p2 = i[int(len(i)/2) + 1:]   # character from len(i)/2+1 index to last index are stored in p2 as we have to skip middle character
        
    p1 = sorted(p1) #sorting both p1 and p2
    p2 = sorted(p2)
    if p1 == p2:
        print('YES')
    else:
        print('NO')