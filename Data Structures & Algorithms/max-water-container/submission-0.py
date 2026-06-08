class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current area
            width = right - left
            current_height = min(heights[left], heights[right])
            current_area = current_height * width
            
            # Update max area if current area is greater
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter bar inward
            if heights[left] < heights[right]:
                left += 1  # Move right
            else:
                right -= 1 # Move left
                
        return max_water