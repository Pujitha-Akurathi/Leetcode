class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set(nums)
        for i in s:
            l=nums.count(i)
            if(l==1):
                return i

        