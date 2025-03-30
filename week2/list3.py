stack = []

def push(val):
    if len(stack)<5:
        stack.append(val)
    else:
        print("Stack overflow")

def pop():
    if len(stack)>0:
        return stack.pop()
    else:
        print("Stack underflow")

def menu():
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    return int(input("Choose an option: "))

while True:
    option = menu()
    if option == 1:
        push(int(input("Enter a number: ")))
    elif option == 2:
        print(pop())
    elif option == 3:
        break
    else:
        print("Invalid option")