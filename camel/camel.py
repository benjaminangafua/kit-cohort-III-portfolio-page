case = input("camelCase: ")

for c in case:
    if c.isupper():
        c = c.replace(c, f"_{c.lower()}")
        print(c,end="")
    else:
        c= c.lower()
        print(c,end="")
print()