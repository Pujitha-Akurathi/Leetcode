from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key=lambda x: x*10, reverse=True)
        s = "".join(nums)
        return "0" if s[0] == "0" else s
