prefix = "my name is"
names = ["ofek", "idan", "eden", "or", "aviran", "avidan", "daniel"]
for name in names:
    print(f"looking for or... currently it is: {name}")
    if name == "or":
        ...
    else:
        print("did not file or")
    print("did not find or yet...")
else:
    print("did not find or at all")


print(names)
names_with_z_containing_dan = []
for name in names:
    if name.find("dan") > -1:
        names_with_z_containing_dan.append(name)

names_with_z_containing_dan = [name + "z" for name in names if name.find("dan") > -1]
for name in names_with_z_containing_dan:
    print(name)
print(names_with_z_containing_dan)

age = int(input("enter your age"))
while age < 50:
    print("you are still ok")
    print("you are still young")
    print("all good")
    age = age + 5
    # age = int(input("enter your age"))
else:
    print("you are old enough")

for i in range(len(names)):
    names[i] = names[i] + "z"
print(names)