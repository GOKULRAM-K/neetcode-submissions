class Solution:
    def findMin(self, nums: List[int]) -> int:
        # b = 0
        # e = len(nums) - 1
        # mid = (b + e) // 2
        # minimum = float('inf')
        # while (nums[mid-1] < nums[mid]):
        #     mid -= 1
        # return min(nums[b], nums[e], nums[mid])
        return min(nums)