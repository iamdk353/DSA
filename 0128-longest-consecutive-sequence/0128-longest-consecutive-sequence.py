class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq=0

        map=set(nums)

        for i in map:
            if i-1 not in map:
                count=1
                while((i+count) in map ):
                    count+=1
                maxSeq=max(maxSeq,count)
        return maxSeq
