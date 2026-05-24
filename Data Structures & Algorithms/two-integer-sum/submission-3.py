class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            r = target - num

            if r in d:
                return [d[r], i]
            d[num] = i