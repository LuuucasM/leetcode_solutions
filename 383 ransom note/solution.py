from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        note = Counter(ransomNote)

        for key in note.keys():
            if key not in letters.keys():
                return False
            if note[key] > letters[key]:
                return False
        return True