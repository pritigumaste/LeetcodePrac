#Time: O(n^2) as we creating copies of the list at every step
#space: O(h) 

#https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        currList =[]
        self.helper(root, currList, 0, targetSum)
        return self.result

    def helper(self,root, currList, currSum, target):
        if root is None:
            return 

        currSum += root.val
        path =[]
        #WOW 
        #so we crated new list and kept on updating it
#we are creating a diff list at every level that way we are not having issue with respect to pointing to 
        #the same list
        path.extend(currList)
        path.append(root.val)
        #print("currList", currList)
        #print("path", path)
              
        if root.left == None and root.right == None:
            if currSum == target:
                #path.append(currList)
                self.result.append(path)
        #print(self.result)
        
        self.helper(root.left, path, currSum, target)
        self.helper(root.right, path, currSum, target)
        

        #this is passing the reference of CURRLIST, hence whenever you are popping
        #it pops an element from the reuslt as well 

       # currList.pop()
       # print("after pop",self.result)
        #currList.remove(len(currList) -1)


        #iterative sol
    #     result =[]
    #     currSum = 0
    #     currList =[]
    #    # st=[]
         
    #     if root is None:
    #         return 
    #     while root != None or st != []:        
    #         while root != None:
    #             currList.append(root.val)
    #             currSum += root.val
    #             root = root.left
    #         print(root)
    #         #root = st.pop()
    #         if root.left == None and root.right==None:
    #             if currSum == targetSum:
    #                 result.append(currList)
    #         root = root.right
    #         print(currList)
    #         currList.remove(len(currList) -1)
    #         #print(currList)
            
            
    #     return result

        
