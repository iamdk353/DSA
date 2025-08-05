def isDisjoint(a,b):
  globSet=set(a)
  
  for i in b:
    if i in globSet:
      return False
  return True

a=[1,2,3,4,5,6,7,8,9,10]
b=[11,12,13]
print(isDisjoint(a,b))
