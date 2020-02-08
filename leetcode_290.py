# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        index = 0
        string = str.split()
        dic = {}
        dic2 = {}
        if len(pattern) != len(string):
            return False

        for p in pattern:
            if not p in dic:
                if string[index] in dic2:
                    return False
                dic[p] = string[index]
                dic2[string[index]] = p
            else:
                if dic[p] != string[index]:
                    return False
            index += 1

        return True