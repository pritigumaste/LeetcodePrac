#Time: 2^n*m (combinations can be possible and we are explorign all of them)
#m being the value of the amount if we are choosing or not
#Space: O^n2 (for every element we generate new copy of path)
#https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(candidates, val, i , path):
            #result= []
            #base
            if i == len(candidates) or val <0:
                return  
        
            #as we are subtratcing target from the number that we are choosing, 
            #we also need to check if target is not 0

            if val ==0:
                result.append(path)
                return  

            #if we dont choose
            #created a copy because we are sending a new reference 
            #so that the same value doesn't get updated. 
            #list was going as a reference 
           
            # we can also change the order of the calls, if we choose before, we will also 
            #have to remove the elements from the path, hence use path.pop()

            helper(candidates, val, i+1, path.copy()) 
            #if we choose 
            path.append(candidates[i])
            helper(candidates, val - candidates[i], i , path.copy())
            #path.pop()

            
        
        result= []
        if len(candidates) == 0:
            return []

        helper(candidates, target, 0 , [])
        #i is the index of the element that we are choosing right now 
        #[] is list of all the elements so far

        return result
        
