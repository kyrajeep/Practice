x = ["a", "b", "c" ,"d"]

x.sort(reverse = True)
print(x)

capital = [y.capitalize() for y in x]
#can put for loop inside the list!!
print(capital)

capital.remove("D")
print(capital)

capital.insert(1,["A", "B"])
print(capital)
capital.pop(3)
print(capital)


