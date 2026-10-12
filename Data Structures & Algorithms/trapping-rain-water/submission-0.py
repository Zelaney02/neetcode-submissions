class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        total = 0

        while left < right:
            if height[left] < height[right]:
            
                if left_max < height[left]:
                    left_max = height[left]

                # max water for curr ind 
                total += left_max - height[left]

                left += 1
            else:
                if right_max < height[right]:
                    right_max = height[right]

                total += right_max - height[right]

                right -= 1

        return total