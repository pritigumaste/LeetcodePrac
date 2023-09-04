# TIME COMPLEXITY = O(nlogn)
#    dividing the array into n havles - logn time 
#    merging them back traversing will take O(n) time '

# SPACE COMPLEXITY = O(n)
# we used extra array for temp storing elements

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we will be using sorting algorithm here 
        temp =[0] * len(nums)
        #temp =[] list index out of range exception if you dont define the size of arr
        def mergeArrays(left: int, mid: int, right: int):
            #splitiing the array into 2 halves
            s1 = left
            s2 = mid+1
            end1 = mid - left+1
            end2= right - mid

            #creating copies of the subarrays in temp array
            for i in range(end1):
                temp[s1 + i] = nums[s1+i]
            for i in range(end2):
                temp[s2+i] = nums[s2+i]

            #merging them back and sorting simultaneously 
            i,j,k=0,0, left
            while i<end1 and j< end2:
                if temp[s1+i] <= temp[s2+j]:
                    nums[k] =temp[s1+i] #copying element back into original arr
                    i+=1
                else:
                    nums[k] =temp[s2+j]
                    j+=1
                k+=1
            
            #copy all the remaining elements once an array is completed after comparing
            while i< end1:
                nums[k] = temp[s1+i]
                i+=1
                k+=1
            while j < end2:
                nums[k] = temp[s2+j]
                j+=1
                k+=1

        #recursive func to make recursive calls 
        def mergeSort(left:int, right: int):
            if left>=right:
                return 
            mid = (left+right) //2
            #merge the first and second halves
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            #merge the sorted halves
            mergeArrays(left, mid, right)
        
        mergeSort(0, len(nums)-1)
        return nums
