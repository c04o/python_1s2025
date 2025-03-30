numbers = list()

def add_n():
    n = int(input("Input number: "))
    if n>18 and n%2!=0:
        numbers.append(n)
    else:
        print("Not valid")

def print_nums():
    print("Numbers:")
    for n in numbers:
        print(n)

while True:
    add_n()
    print_nums()
    if input("Add a new number? (y/n): ").lower() != "y":
        break

print_nums()