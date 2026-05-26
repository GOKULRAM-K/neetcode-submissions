class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack  =[]
        m_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = (i-index) * height
                m_area = max(m_area, area)
                start = index
            stack.append((start, heights[i]))

        for index, height in stack:
            area = height*(len(heights)-index)
            m_area = max(area, m_area)
        return m_area