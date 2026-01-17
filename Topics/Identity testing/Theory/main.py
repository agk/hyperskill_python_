#  You can experiment here, it won’t be checked
a = 100000
b = 100000

print(bool(a is b))
print(bool(id(a) == id(b)))
print(bool(a == b))
print(bool(id(a) is id(b)))

#x = 25 % 12 # 1
#8 % y = 3 # 5
#8 mod y=3
#z mod 6=1,если  8<z<18
# 13

x = 19%12
y = (2*x) % 5
print(x, y)

inf = float('inf')
print(1 / inf)
# print(1 / 0) # error
print(0 * inf)