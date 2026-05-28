class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = int((start+end)/2)
        while (start < end):
            if target < nums[mid]:
                end = mid-1
                
            elif target > nums[mid]:
                start = mid+1
                
            else:
                return mid
            
            mid = int((start+end)/2)
        if nums[mid]==target:
            return mid
        return -1
        