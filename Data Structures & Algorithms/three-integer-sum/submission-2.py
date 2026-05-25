class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while (left < right):
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    a = [nums[i], nums[left], nums[right]]
                    if a not in l:
                        l.append(a)
                    left+=1
                    right-=1
                elif target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
            # left += 1
            # right -= 1
        return l