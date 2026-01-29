class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        low=0
        high=len(height)-1

        while(low<high):
            containerHeight=min(height[low],height[high])
            containerWidth=high-low

            maxArea=max(maxArea,containerHeight*containerWidth)
            
            if(height[low]<height[high]):
                low+=1
            else:
                high-=1

        return maxArea

