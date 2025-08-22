class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s[::-1]
        s1 = ""
        for ch in l:
            if ch == ' ':
                if s1:
                    break
                else:
                    continue
            else:
                s1 += ch
        return len(s1)
