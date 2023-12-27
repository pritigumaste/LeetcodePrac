#time : o(m*n) - time required to traverse a matrix.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result =[]
        row= len(matrix)
        col = len(matrix[0])
        r,c =0,0
        rlast = row-1
        clast= col-1
        
        # dont use the same variables for iterating and also when you are referring to something
        while len(result) < row *col:
            for i in range(c,clast+1):
                result.append(matrix[r][i])
            #r+=1
            for i in range(r+1, rlast+1):
                result.append(matrix[i][clast])
            #clast -=1
            if r != rlast:
                for i in range(clast-1, c-1, -1):
                    result.append(matrix[rlast][i])
            #rlast -=1
            #clast -=1
            if c != clast:
                for i in range(rlast-1 , r, -1):
                    result.append(matrix[i][c])
            c+=1
            r+=1
            rlast -=1
            clast -=1
        return result

#ONE MORE SOLUTION BELOW 
-----------------------------------------------------------------------------------------

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []

        left =0 
        right = n-1
        top = 0
        bottom = m-1
        #to ensure boundary conditions are met, we need to check that these don't 
        #cross each other
        while(top <= bottom and left <= right):

            #traversing top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            #once row 0 is iterated we are never coming back again 
            #so need to increment the row number to next one
            top +=1

            #traversing right col
            #no need to check base condition here because we aren't modifying 
            #left and right before proceeding 
            #if (top <= bottom and left <= right):
            for j in range(top, bottom+1):
                result.append(matrix[j][right])
            #decrementing the column number 
            right -=1

            #print(matrix[bottom][right])
            #traversing bottom row 
            if (top <= bottom):
                for k in range(right , left-1, -1):
                #print(matrix[bottom][k])
                    result.append(matrix[bottom][k])
            #incrementing the row number
            
            bottom -=1 

            
            if (left <= right):
            #traversing left col 
                for l in range(bottom, top-1, -1):
                    result.append(matrix[l][left])
            left+=1


        
        return result 




        
