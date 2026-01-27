class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for i in range(0,len(nums)):
            diff = target- nums[i]
            if diff in prev:
                return [prev[diff],i]
            prev[nums[i]]=i



