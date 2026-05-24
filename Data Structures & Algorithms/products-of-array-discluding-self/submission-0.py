class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        m1 = [nums[0]]

        for i in nums[1:]:
            m1.append(m1[-1] * i)

        m2 = [0] * len(nums)
        m2[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            m2[i] = m2[i+1] * nums[i]

        l = []
        for i in range(len(nums)):
            v = 0
            if i==0:
                v = m2[i+1]
            elif i==len(nums)-1:
                v = m1[i-1]
            else:
                v = m1[i-1] * m2[i+1]
            l.append(v)
        return l