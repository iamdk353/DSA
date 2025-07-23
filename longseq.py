def longestConsecutive( nums) -> int:
    longest=0
    numSet=set(nums)
    # {1,2,7,4,3,5}
    for i in numSet:
        length=0
        if i-1 not in numSet:
            while length+i in numSet:
                length+=1
            longest=max(longest,length)
    return longest

longestConsecutive([2,20,4,10,3,4,5])