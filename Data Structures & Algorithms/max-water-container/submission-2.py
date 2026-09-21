class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(i, j):
            area = min(heights[i], heights[j]) * abs(i - j)
            return area
        
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            if area(i, j) > max_area:
                max_area = area(i, j)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area


        