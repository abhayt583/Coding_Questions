class Solution:
    def maxArea(self, height: List[int]) -> int:
        one=0
        two=len(height)-1

        max_area=0

        while one<=two:
            width=two-one
            if height[one]<height[two]:
                area=height[one] * width
                one=one+1
            else:
                area=height[two]*  width
                two=two-1

            if area>max_area:
                max_area=area
            else:
                max_area=max_area
            
        return max_area
