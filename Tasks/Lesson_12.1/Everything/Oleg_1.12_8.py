s = input()
name = input()

f = open(name, 'a')
f.write(s)
f.close()