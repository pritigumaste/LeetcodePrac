class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(nums, i , arr):
            #base condition
            if (i==len(nums)):
                result.append(arr.copy())
                return
            #if not choose
            helper(nums, i+1, arr)
            #if choose 
            arr.append(nums[i])
            helper(nums, i+1 , arr)
            arr.pop()

        
        if len(nums) ==0:
            return 
        result=[]
        helper(nums, 0, [])
        return result
        
