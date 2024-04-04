#time: O(n) will iterate once
#space: O(min(m,n)) m is the number of chars/ n is the size of string
#depending on what we store in hashMap

#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left =0 
        hashMap = {}
        result =0 

        for right in range(len(s)):
            hashMap[s[right]] = 1+ hashMap.get(s[right], 0)

            while(max(hashMap.values()) > 1):
                hashMap[s[left]] -=1
                left +=1 
            result = max(right - left +1, result)
        return result
