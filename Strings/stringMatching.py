
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#SLIDING WINDOW
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        big = len(haystack)
        small = len(needle)

        for win in range(big-small +1):
            for i in range(small):
                #we will break from loop if the letters aren't same
                if needle[i] != haystack[win+i]:
                    break
            
                #when we reach the last element of the smaller word
                #we know that we have traversed it fully hence we return the index 
                #from where we started the smallest word in the bigger word
                if i == small -1:
                    return win
        
        return -1
