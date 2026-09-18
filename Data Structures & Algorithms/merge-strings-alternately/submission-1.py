class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        merged_s = ""
        m = len(word1)
        n = len(word2)

        while i < m or j < n:
            if i < m:
                merged_s += word1[i]
                i += 1
            if j < n:
                merged_s += word2[j]
                j += 1
    
        return merged_s

        

            
        