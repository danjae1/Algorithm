a=True
b=True
c=False

r1 = not a
r2 = a and b
r3 = a or b
r4 = a and (b or c)
r5 = a or (b and c)
r6 = not a or (b and not c)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)