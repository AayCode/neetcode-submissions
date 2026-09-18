class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        merged_s = ""
        m = len(word1)
        n = len(word2)

        while i < m or j < n:
            if i < m and j < n:
                merged_s += word1[i]
                merged_s += word2[j]
                i += 1
                j += 1
            elif i < m:
                merged_s += word1[i:m]
                return merged_s
            else:
                merged_s += word2[j:n]
                return merged_s
        return merged_s

        

            
        