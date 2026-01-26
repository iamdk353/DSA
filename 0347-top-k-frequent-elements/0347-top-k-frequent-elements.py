
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[]
        freq={}
        for i in range(len(nums)+1):
            bucket.append([])
        
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for value,repn in freq.items():
            bucket[repn].append(value)
        
        res=[]
        for i in range(len(nums),0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
