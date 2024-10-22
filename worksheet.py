a = 15
b = 12
print(type(a))
print(type(b))

print(f"a +b = {a +b}")
print(f"a -b = {a -b}")
print(f"a *b = {a *b}")
print(f"a /b = {a /b}")

c = int(a/b)
print(c)
print(type(c))

b = float(c)
print(b)
print(type(b))

print(f"The result of a divided by b is{c}")

if a > b :
    print("True")
else:
    print("False")
if a ==b :
    print("True")
else:
    print("False")