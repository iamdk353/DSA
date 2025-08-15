def TwoSum(a,target):
  
  aHash={}
  for i,v in enumerate(a):
    diff=target-v
    if diff in aHash:
      return  [aHash[diff],i]
    aHash[v]=i