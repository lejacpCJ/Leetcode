class Solution:
    def sortVowels(self, s: str) -> str:
        s_list = [c for c in s]
        vowels = []
        indexs = []

        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                vowels.append(c)
                indexs.append(i)
        vowels.sort()

        for i in range(len(indexs)):
            s_list[indexs[i]] = vowels[i]

        return ''.join(s_list)