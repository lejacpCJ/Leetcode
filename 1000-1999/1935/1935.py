class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = text.split()
        res = 0

        for word in lst:
            isValid = True
            for char in brokenLetters:
                if char in word:
                    isValid = False
                    break
            if isValid:
                res += 1
        return res