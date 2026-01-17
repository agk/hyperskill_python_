#  You can experiment here, it won’t be checked
a = 100000
b = 100000

print(bool(a is b))
print(bool(id(a) == id(b)))
print(bool(a == b))
print(bool(id(a) is id(b)))