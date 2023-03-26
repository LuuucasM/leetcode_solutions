class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = [nums[0]]
        for num in nums[1:]:
            running_sum.append(running_sum[-1]+num)
        return running_sum
    

