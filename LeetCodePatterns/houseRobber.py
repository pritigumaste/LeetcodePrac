


class Solution:

    #this will give TLE 
    #NEED TO USE MEMOIZATION 
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        #using set because it avoids redundancy 
        
        self.mem = {}
        return self.check(0, nums)

    def check(self, i , nums):
        sumMax =0 
        if i >= len(nums):
            return 0

        if i in self.mem:
            return self.mem[i]

        sumMax = max(self.check(i+2, nums) + nums[i], self.check(i+1, nums))
        #print(nums[i+2], "nums[i+2")
        # print(nums[i], "nums[i]")
        # print(sumMax)
        self.mem[i] = sumMax
        return sumMax
        




-----------------------------------------------------------------------
#Time is EXPONENTIAL 
#this will give TLE 
    #NEED TO USE MEMOIZATION 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        return self.check(0, nums)

    def check(self, i , nums):
        sumMax =0 
        if i >= len(nums):
            return 0

        sumMax = max(self.check(i+2, nums) + nums[i], self.check(i+1, nums))
        #print(nums[i+2], "nums[i+2")
        # print(nums[i], "nums[i]")
        # print(sumMax)
        return sumMax
        
