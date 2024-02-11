#https://leetcode.com/problems/counting-bits/
#time: O(nlogn) logn operations for n numbers
#space: O(1) output array we won't count

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(n+1):
            var =0
            while i !=0:
                i &= (i-1)
                var+=1
            result.append(var)
        return result
        
