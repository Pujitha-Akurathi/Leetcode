class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        sum=0
        while(x>0):
            digit=x%10
            sum=sum*10+digit
            x=x//10
        if num==sum:
            return True
        else:
            return False

        