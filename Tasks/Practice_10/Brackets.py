def Add(s):
  if(len(s) == 2 or len(s) == 1):
     return s
  else:
    return s[0] + "(" + Add(s[1:-1]) + ")" + s[-1]
s = input()

print(Add(s))
