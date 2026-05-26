class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = (i-index) * height
                max_area = max(max_area, area)
                start = index
            stack.append((start, heights[i]))
        for index, height in stack:

            area = height * (len(heights) - index)

            max_area = max(max_area, area)

        return max_area