# Name = Rajput Akshaykumarsing Virendra
# ID = 20cs069

class myStack:

    def __init__(self):
        self.my_stack = []

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        if self.is_Empty():
            print("Stack underflow!")
        else:
            return self.my_stack.pop()

    def is_Empty(self):
       return len(self.my_stack) == 0
   
    def traversal(self):
        print(f'stack =  {self.my_stack[::-1]}')


stk = myStack()

print("Enter from below option : \n")
while True:
    print("1. PUSH")
    print("2. POP")
    print("3. TRAVERSAL")
    print("4. QUIT.")

    option = int(input('Enter your choice:'))

    if option == 1:
        element = int(input('Enter value:'))
        stk.push(element)
    elif option == 2:
        print(f"Removed: {stk.pop()}")
    elif option == 3:
        stk.traversal()
    elif option == 4:
        break
    else:
        print("Enter correct choice!")