#Time complexity: O(n+k) - iterating over orginal array and input array's range again so k for that
#space complexity: O(n) we using hashMap to store values 

#Highly used when the range of elements is limited.
#Count the frequency of elements and the compare and input the elements in crt positions based on values 
#non-comparitive algo 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Counting Sort

        def countSort():
            counts ={}
            minVal = min(nums)
            maxVal = max(nums)

            #update the frequency as we find new elements in nums
            for val in nums:
                counts[val] = counts.get(val, 0) + 1

            index =0
            #sorting part
            #easier to sort if we starting from smallest value             
            for val in range(minVal, maxVal+1, 1):
                #arrange all similar values together
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index +=1
                    counts[val] -=1
        
        countSort()
        return nums


