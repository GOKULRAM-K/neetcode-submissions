class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1
        mid = (b + e) // 2

        while (b <= e):
            if nums[mid] == target:
                return mid
            if nums[b] <= nums[mid]:
                if nums[b] <= target < nums[mid]:
                    e = mid - 1
                else:
                    b = mid + 1
            else:
                if nums[mid] < target <= nums[e]:
                    b = mid + 1
                else:
                    e = mid - 1
            mid = (b + e) // 2
        return -1
                


            
