from typing import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)  #EASY METHODS
        # return Counter[s] == Counter[t]
        counts = {}
        countt = {}
        if len(s) == len(t):
            for i in range(len(s)):
                counts[s[i]] = 1 + counts.get(s[i], 0)
                countt[t[i]] = 1 + countt.get(t[i], 0)
            for c in counts:
                if counts[c] != countt.get(c,0):
                    return False
            return True
        else:
            return False


a = Solution()
s = "rat"
t = "car"
print(a.isAnagram(s, t))
