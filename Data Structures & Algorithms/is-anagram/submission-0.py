class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            lookup = {}
            for i in s:
                if i not in lookup:
                    lookup[i] = 0
                lookup[i] += 1
            for j in t:
                if j in lookup and lookup[j] > 0:
                    lookup[j] -= 1
                else:
                    return False
            return True
        return False
        