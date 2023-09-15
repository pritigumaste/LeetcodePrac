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

            
