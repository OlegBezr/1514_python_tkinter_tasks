a, b = input().split()
a = int(a)
b = int(b)

b1 = b

while (a > 0):
    a, b = b % a, a

b1 /= b

while (b1 % 2 == 0):
    b1 /= 2
while (b1 % 5 == 0):
    b1 /= 5

if (b1 == 1):
    print('yes')
else:
    print('no')