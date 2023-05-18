class Solution:
    def partitionString(self, s: str) -> int:
        total = []
        sub_str = ""
        for letter in s:
            if letter not in sub_str:
                sub_str += letter
            else:
                total.append(sub_str)
                sub_str = letter
        total.append(sub_str)
        return len(total)