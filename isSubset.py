def isSubset(a,b):
 
  if len(a) < len(b):
    GlobSet=set(a)
  else : 
    GlobSet=set(b)
  
  for i in b:
    if i not in GlobSet:
      return False
    
  return True

a=[1,2,3,4,5,6,7,8,9]
b=[4,7,9,1]
print(isSubset(a,b))
