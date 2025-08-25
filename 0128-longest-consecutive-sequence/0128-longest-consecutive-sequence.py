from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()    
        l = [nums[0]] 

        for i in nums[1:]:
            if i != l[-1]: 
                l.append(i)

        longest = 1
        current = 1

        for i in range(1, len(l)):
            if l[i] - l[i-1] == 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1 

        return longest
