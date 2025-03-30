age = int(input("how old are you?: "))
if age >= 60:
    print("third age")
elif age >= 18:
    print("adult")
elif age >= 13:
    print("teen")
elif age >= 0:
    print("child")
else:
    print("invalid age")