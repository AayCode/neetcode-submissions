class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = cur_len = max_len = 0
        seen = set()

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                cur_len -= 1
                i += 1

            seen.add(s[j])
            cur_len += 1
            max_len = max(cur_len, max_len)

        return max_len

