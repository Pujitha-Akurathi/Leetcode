class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            sum=0
            while n>0:
                digit=n%10
                sum+=digit*digit
                n=n//10
            n=sum
            if n in seen:
                return False
            seen.add(n)
        return True
