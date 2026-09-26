class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_bar = 0
        right_bar = n - 1
        max_area = 0
        
        while right_bar > left_bar:
            height = min(heights[left_bar], heights[right_bar])
            width = right_bar - left_bar

            max_area = max(max_area, height*width)

            if heights[left_bar] <= heights[right_bar]:
                left_bar += 1

            elif heights[left_bar] > heights[right_bar]:
                right_bar -= 1

        return max_area