#Time Complexity: O(nlogn)
#  logn for traversing the height of binary tree 
#  n because we will have to heapify for n elements n times 

#Space Complexity O(logn)
#space taken by recursive stack

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(n: int, i:int):
            #assign largest as i
            #cal len of left and right nodes
            largest = i
            leftNode = 2*i + 1
            rightNode = 2*i+2

            #assign largest as leftNode if that is the largest
            #n is len of nums
            if leftNode < n and nums[leftNode] > nums[largest]:
                largest = leftNode
            
            #assign largest as rightNode if that is the largest
            if rightNode < n and nums[rightNode] > nums[largest]:
                largest = rightNode
            
            if largest != i:
                #swapping using comma operator
                nums[i] , nums[largest] = nums[largest], nums[i]
                heapify(n, largest)
        
        def heapSort():
            n= len(nums)

            #as we are following top down approach 
            #we heapify all elements from top to down 

            #for loop means we traversing from top most ele to leaf node 
            #practically -1 =th node and reducing the index by -1 ayt each step
            #hence (n//2, -1, -1)
            for i in range(n//2, -1, -1):
                heapify(n,i)
            
            #traversing elements for swapping curr root to end.
            for i in range(n-1, -1, -1):
                nums[0], nums[i] = nums[i] , nums[0]
                heapify(i,0)
        heapSort()
        return nums
