class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m = -1
        running_tot = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running_tot += 1
            else:
                m = max(m, running_tot)
                running_tot = 0
        m = max(m, running_tot)
        return m