from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        l = []
        i = 0
        while i < len(chars):
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            l.append(chars[i])
            if count > 1:
                for c in str(count):
                    l.append(c)

            i += 1
        for j in range(len(l)):
            chars[j] = l[j]

        return len(l)
