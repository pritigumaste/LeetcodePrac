#CONTAINER WITH MOST WATER 
#https://leetcode.com/problems/container-with-most-water/description/
#Time - o(n) as we are traversing the list only once

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #TWO POINTERS
        area =0
        left =0
        right = len(height) -1

        while left< right:
            wid = right - left
            area = max(area, min( height[left], height[right]) * wid)
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
                 
        return area
