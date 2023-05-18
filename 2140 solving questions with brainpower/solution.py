from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]

        for i in range(len(questions) - 2, -1, -1):
            if i+questions[i][1]+1 < len(questions):
                dp[i] = max(dp[i+1], questions[i][0]+dp[i+questions[i][1]+1])
            else:
                dp[i] = max(dp[i+1], questions[i][0])
        return dp[0]