class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1-nums2), list(nums2-nums1)]