class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            left_max = height[i]
            right_max = height[i]
            for j in range(i, -1, -1):
                if height[j] > left_max:
                    left_max = height[j]
                    # break
            for j in range(i, len(height)):
                if height[j] > right_max:
                    right_max = height[j]
                    # break
            area = area + min(right_max, left_max) - height[i]
        return area
            
        