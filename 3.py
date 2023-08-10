a = "aviel 'buskila'"
b = 'aviel buskila'
c = "aviel \"buskila\""
d = "devops experts"
h = {"fname": "aviel",
     "lname": "naor",
     "age": 33,
     "is_married": True,
     "hobbies": ["bicycle", "guitar"]}
i = ("aviel", "buskila", 34, True)
k = ["aviel", "buskila", 34, True]
print(i[2])
k[2] = 35
print(b + " from " + d)
e = f"his name is {h['fname']} {h['lname']} and his hobbies are {h['hobbies']}"
print(e)
g = "%s %s" % (b, d)
print(g)
# join
print(b + str(k[2]))
print("* ".format(h["hobbies"]))