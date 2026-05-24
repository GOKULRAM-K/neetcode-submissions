class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = list(set(nums))
        nums.sort()
        a = []
        aa = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                aa+=1
            else:
                a.append(aa)
                aa=1
            
        a.append(aa)
        return max(a)

