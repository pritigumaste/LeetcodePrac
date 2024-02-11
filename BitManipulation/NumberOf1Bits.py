#https://leetcode.com/problems/number-of-1-bits/
#time: O(1) #more like the number of bits worst case if all bits are 1 else its constant time
#space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum =0

        while n!=0:
            sum +=1
            n &= (n-1)

        return sum
        
