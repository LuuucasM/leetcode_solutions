class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        dp = [[0 for _ in range(len(satisfaction)+2)] for _ in range(len(satisfaction)+1)]

        for i in range(len(satisfaction)-1, -1, -1):
            for j in range(1, len(satisfaction)+1):
                dp[i][j] = max((satisfaction[i] * j) + dp[i+1][j+1], dp[i+1][j])
        return dp[0][1]