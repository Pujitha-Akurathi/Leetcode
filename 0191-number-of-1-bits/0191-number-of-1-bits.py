class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)[2:]
        s=0
        for i in x:
            if i=='1':
                s+=1
        return s