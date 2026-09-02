class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for k in range(len(strs[0])):
            char = strs[0][k]

            for s in strs:
                if k >= len(s) or s[k] != char:
                    return result

            result += char

        return result
