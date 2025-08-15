def MaxWater(heights)->int:
  low=0
  high=len(heights)-1
  maxArea=0

  while low<high:
    width=high-low
    height=min(heights[low],heights[high])
    maxArea=max(maxArea,width*height)

    if heights[low] < heights[high]:
      low+=1
    else:
      high-=1
  return maxArea
print(MaxWater([1,8,6,2,5,4,8,3,7]))
