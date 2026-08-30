class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha() or abbr[j] == '0':
                return False
            else:
                number = 0
                while j < len(abbr) and abbr[j].isdigit():
                    number = number * 10 + int(abbr[j])
                    j += 1
                i = i + number

        return i == len(word) and j == len(abbr)

                        

