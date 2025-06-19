
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Helper function to calculate the maximum area recursively
        def calculate_max_area(i, j, max_area):
            # Base case: If j reaches the end of the array, return the max_area
            if j == len(height):
                return max_area
            
            # Calculate the area between the lines
            area = min(height[i], height[j]) * (j - i)
            
            # Update max_area if the current area is greater
            max_area = max(max_area, area)
            
            # Recursively call calculate_max_area with updated indices
            if i == j - 1:  # Check if i needs to be incremented
                return calculate_max_area(0, j + 1, max_area)
            else:
                return calculate_max_area(i + 1, j, max_area)
        
        # Start the recursion with initial indices and max_area set to 0
        return calculate_max_area(0, 1, 0)





