from typing import List

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = [int(x) for x in version1.split('.')]
        lst2 = [int(x) for x in version2.split('.')]

        if len(lst1) > len(lst2):
            for i in range(len(lst1) - len(lst2)):
                lst2.append(0)
        elif len(lst2) > len(lst1):
            for i in range(len(lst2) - len(lst1)):
                lst1.append(0)

        for i in range(len(lst1)):
            if lst1[i] > lst2[i]:
                return 1
            elif lst1[i] < lst2[i]:
                return -1
        return 0