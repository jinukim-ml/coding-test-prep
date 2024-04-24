from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        # two arrays
        # first array: max_left_height
        # second array: max_right_height
        left_max = 0
        right_max = 0
        left_tallest = []
        right_tallest = []
        
        for i in range(n):
            left_height = height[i]
            right_height = height[n-(i+1)]
            if left_max < left_height:
                left_max = left_height
            if right_max < right_height:
                right_max = right_height
            
            left_tallest.append(left_max)
            right_tallest.append(right_max)

        for i in range(len(height)):
            water = min(left_tallest[i], right_tallest[n-i-1]) - height[i]
            if water:
                area += water

        return area