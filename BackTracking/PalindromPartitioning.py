#time: O(n*2^n)
#space: O(n)
#https://leetcode.com/problems/palindrome-partitioning/

#01 recursion

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #we need to maintain 2 indices one with the index for the substring and one wiht 
        #the index that is traversing the whole string
        def check(substring):
            start=0
            end = len(substring)-1
            while start<=end:
                if substring[start]!=substring[end]:
                    return False
                start+=1
                end-=1
            return True 

        def helper(s, ch, index , arr):
            if index == len(s):
                result.append(arr)
                return

            if ch == len(s):
                return 
            
            #not choose 
            #then our subs index stays there but we incraese our search scope 
            #and move to the next index
            helper(s, ch+1,index ,arr.copy())

            #choose
            #we take the substring first check if its palindrome 
            substring = s[index: ch+1]
            if (check(substring)):
                arr.append(substring)
                #now that we have chose our subs, our new indices are starting from ch+1 in the
                #next iteration
                helper(s, ch+1, ch+1 , arr.copy())
                #arr.pop()

        if len(s) ==0:
            return 
        result= []
        helper(s, 0 ,0, [])
        return result
        
