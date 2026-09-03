class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for k in range(len(strs[0])):
            for s in strs:
                if k == len(s) or s[k] != strs[0][k]:
                    return result
                
            result += strs[0][k] 

        return result 