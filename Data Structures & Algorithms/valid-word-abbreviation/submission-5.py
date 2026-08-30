class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0

        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                
            else:
                if abbr[j] != '0':
                    number = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        number = number * 10 + int(abbr[j])
                        j += 1
                    i += number

                else:
                    return False
        return i == len(word) and j == len(abbr)
                        

