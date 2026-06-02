class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = nums
        slow = num[0]
        fast = num[0]

        while slow:
            slow = num[slow]
            fast = num[num[fast]]

            if slow == fast:
                break
        
        slow = num[0]
        while slow!=fast:
            slow = num[slow]
            fast = num[fast]

        return slow
        