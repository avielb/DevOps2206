isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
my_list = ["1", "2"]
is_age_above_twentyfour = (a == 24 or strOne == "One")
is_not_aviel = (strThree == "aviel")
if isTrue and is_age_above_twentyfour and is_not_aviel:
    print("true and two")
elif is_age_above_twentyfour and b == 2.5:
    print("blabla2")
else:
    print("balbla")

if len(my_list) > 0:
    print("I have items")
else:
    print("i dont items")