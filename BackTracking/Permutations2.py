#https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def helper(arr,counter):
            #running it till the whole array is traversed 
            if len(arr) == len(nums):
                result.append(arr.copy())
                return 
            #the order was important here, so we need to use a data structure 
            #in order to make sure that we are accessing the "count" of values and then 
            #adding them to the list , we also need to incraese the count for next iteration
            for i in counter:
                if counter[i] > 0:
                    arr.append(i)
                    counter[i] -=1 
                    helper(arr, counter)                    
                    arr.pop()
                    counter[i] +=1
            
        result =[]
        helper([], Counter(nums))
        return result
