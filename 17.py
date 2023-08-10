from exercise import name_of_user

for i in range(100):
    print(i)

def get_input():
    NameOfUser = input("enter your name: ")
    name_of_user = input("enter your name: ")


check_if_name_is_aviel = name_of_user == "aviel"
if check_if_name_is_aviel:
    print("hello" + name_of_user)
