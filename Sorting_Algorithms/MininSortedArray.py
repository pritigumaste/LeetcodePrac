#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low =0
        high = len(nums) - 1

        if len(nums) ==1:
            return nums[0]

        if(nums[high] > nums[low]):
            return nums[low]
        while(low <=high):
            mid= (low+high)//2
            #mid = low + (high-low) //2
            if(nums[mid] > nums[mid+1]):
                return nums[mid+1]
            if(nums[mid-1] > nums[mid]):
                return nums[mid]

            if(nums[mid] > nums[0]):
                low = mid+1
            else:
                high = mid-1
