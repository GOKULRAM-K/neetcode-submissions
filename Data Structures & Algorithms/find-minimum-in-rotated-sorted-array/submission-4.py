class Solution:
    def findMin(self, nums: List[int]) -> int:
        b = 0
        e = len(nums) - 1
        mid = (b + e) // 2
        minimum = float('inf')
        while (b<=e):
            minimum = min(nums[b], nums[e], nums[mid])
            if nums[e] < nums[mid]:
                b = mid+1
            elif nums[e] > nums[mid]:
                e = mid
            else:
                minimum = min(nums[b], nums[e], nums[mid])
                break
            mid = (b+e)//2
        return minimum