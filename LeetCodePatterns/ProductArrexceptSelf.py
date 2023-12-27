#https://leetcode.com/problems/product-of-array-except-self/description/
#time - 0(n)
#space = 0(n) - because we are using extra space to store left and right running products 
#this intution came, if we are to take any random number and are asked for running product 
#then we can say we will need product of numbers at left to product of numbers at right. 
#hence the running product of left and right side of numbers should get us the answer. 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        #to make sure we aren't wasting space by just defining a listwith no size
        result = [0] * length
        leftArray = [0] * length 
        rightArray = [0] * length
        
        leftArray[0] =1 #as no elements to the left

        for i in range(1, len(nums)):
            leftArray[i] = nums[i-1] * leftArray[i-1]

        rightArray[length-1] = 1 # as no elements to right of length-1

        for i in reversed(range(length-1)):
            rightArray[i] = nums[i+1] * rightArray[i+1]

        for i in range(length):
            result[i] = leftArray[i] * rightArray[i]

        return result

            
                
