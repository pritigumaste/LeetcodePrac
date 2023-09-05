#Time complexity: o(n) - as we are traversing the nums array once 
#Space Complexity: o(1) - as we are just using variables only 
#https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       #using kadane's algo
        currArray =nums[0]
        maxArray=nums[0]

        for i in  nums[1:]:
            currArray = max(i, currArray+ i)
            maxArray= max(maxArray, currArray)
        return maxArray
    
        
