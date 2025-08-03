def threeSum(nums):
  nums.sort()
  ans=[]
  n=len(nums)

  for i in range(n):
    if (nums[i] > 0):
      break
    if (nums[i]==nums[i-1]):
      continue
    low=i+1
    high=n-1

    while (low<high):
      curSum=nums[i]+nums[low]+nums[high]
      if (curSum == 0):
        ans.append([nums[i],nums[low],nums[high]])
        low+=1
        high-=1
        while (nums[low]==nums[low-1] and low<high):
          low+=1
        while (nums[high] == nums[high+1] and low<high):
          high-=1
        
      elif (curSum > 0):
        high-=1
      else:
        low+=1
  return ans
print(threeSum([-1,0,1,2,-1,-4]))