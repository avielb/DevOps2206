from os import getenv
print(getenv("TEST"))
print("Hello, World!")
a = 30
b = 5
c = a + b
d = "aviel"
e = True
f = ["1", 2, True, ["aviel", "buskila"]]
g = ["aviel", "naor", 33, True, ["bicycle", "guitar"]]
h = {"fname": "aviel",
     "lname": "naor",
     "age": 33,
     "is_married": True,
     "hobbies": ["bicycle", "guitar"]}
print(f[3][1])
print(h["fname"] + h["lname"])
if h["lname"] == "aviel":
    print("you are aviel")
elif h["is_married"]:
    print("its ok to not be aviel and not be married")

if not -2:
    print("Dor")

