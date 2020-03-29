# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True