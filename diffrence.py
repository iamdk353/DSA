def arithSubArr(a):
  if len(a) < 2:
    return 
  n=len(a) 
  pd=a[1] - a[0]
  cur = 2 
  ans=2
  for i in range(2,n-1):
    if a[i]-a[i-1] == pd:
      cur+=1
      ans=max(ans,cur)
    else:
      cur=2
      pd=a[i]-a[i-1]
  return ans

print(arithSubArr([1,2,3,4,5,6,7,-1]))
