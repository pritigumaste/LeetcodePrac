#Time: O(n) 
#Space: O(m) possible 26 chars

#https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap ={}
        result =0
        left =0
       
        for right in range(len(s)):
            #adding frequency to hashmap count of chars
            hashMap[s[right]] = 1 + hashMap.get(s[right], 0)

            #window(that we are considering now) - max repeated char > k 
            while(right-left+1) - max(hashMap.values()) >k:
                #reducing the char that is to be replaced by 1
                hashMap[s[left]] -=1
                #incrementing the window 
                left +=1
            
            result = max(result, right-left +1)
        
        return result

