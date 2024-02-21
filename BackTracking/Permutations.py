#https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(arr):
            if len(arr) == len(nums):
                result.append(arr.copy())
                return 
            #here you have to iterate over all the values 
            #so better to use for loop 
            
            for n in nums:
                if n not in arr:
                    arr.append(n)
                    helper(arr)
                    arr.pop()

        
        result= []
        if len(nums)==0:
            return 
        helper([])
        return result
        
