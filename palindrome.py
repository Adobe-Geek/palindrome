a = input("what's your string?\n")
b = []
c = []

for el in a[0:]:
    b.append(el)
for le in reversed(a):
    c.append(le)
print(b)
print(c)

if b == c:
    print("palindrome!")
else:
    print("nope")
