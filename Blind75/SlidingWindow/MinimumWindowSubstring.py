class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #base condition
        if len(s) < len(t):
            return ""
        if t =="": return ""

        hashMapT= {} 
        hashMapS ={}
        l=0
        for c in t:
            hashMapT[c] = 1+ hashMapT.get(c, 0)
        
        present, need =0, len(hashMapT)

        result = [-1,-1]
        resLen = float("infinity")
        for r in range(len(s)):
            c= s[r]
            hashMapS[c] = 1+ hashMapS.get(c,0)

            if c in hashMapT and hashMapS[c] == hashMapT[c]:
                present +=1
            
            while present == need:
                if (r-l+1) < resLen:
                    result =[l,r]
                    resLen=(r-l+1)
                hashMapS[s[l]] -=1
                if s[l] in hashMapT and hashMapS[s[l]] < hashMapT[s[l]]:
                    present -=1
                l+=1
        l,r = result
        return s[l:r+1] if resLen != float("infinity") else ""


        

        
