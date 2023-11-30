#https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

#time complexity : o(logn ) 
# space O(1)
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low =0
        high = 1
        while(reader.get(high) < target):
            low = high 
            high = 2 * high 
            #print("inside first while. Low", low , "high:", high)
        while low <= high:
            #mid  = low + ((high-low)/2) 
            mid  = (low + high)//2
            #print("mid", mid)
            if(reader.get(mid) == target):
                return mid
            if(reader.get(mid) > target):
                high = mid-1
            else:
                low = mid+1
        
        return -1

