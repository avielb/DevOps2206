try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a / b)
except ZeroDivisionError as moshe:
    print("you tried to divide by zero, nu nu nu")
    print(moshe.args)
except ValueError as e:
    print("bad input")
    print(e.args)
except BaseException as e:
    print(e.args)
print("aviel")