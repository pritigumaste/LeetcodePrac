#https://leetcode.com/problems/diagonal-traverse/

#time : o(m*n) 
#space : 0(1) as we are not using extra sapce 

#thought process is to come up with boundary condiitons for traversal and just traversing 

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = [0] * m*n  
        r, c =0,0
        direction =1 #initially we need to start traversing from above 
        index =0 
        while (index < len(result)):
            result[index] = mat[r][c]
            index +=1
            #if you check r==0 and c==0 we end up ignoring the extreme conditions
            #so we need to first check the boundary that is if c and r are exceeding 
            #the m-1 and n-1 
            #traversal to next eelemets
            if(direction ==1):
                if c== n-1:
                    r+=1
                    direction =-1 
                elif r==0:
                    c+=1
                    direction = -1 
                else:
                    c+=1 
                    r-=1
                
            else:
                
                if r== m-1:
                    c+=1 
                    direction =1
                elif c== 0:
                    r+=1 
                    direction =1 
       
                else:
                    r+=1 
                    c-=1

        return result 
