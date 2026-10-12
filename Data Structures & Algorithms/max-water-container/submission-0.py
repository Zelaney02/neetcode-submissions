class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            # calculate current area
            width = right - left
            min_height = min(heights[left], heights[right])
            area = min_height * width

            if area > max_area:
                max_area = area

            if min_height == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area
        