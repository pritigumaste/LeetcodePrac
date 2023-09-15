# time - o(n) - n is len of matrix as we traversing twice for reversing and transposing 

class Solution:

    #ROWS BECOME COLS AND COLS BECOME ROWS
    def transpose(self,mat):
        n = len(mat)
        for i in range(n):
            for j in range(i+1, n):
                # we start swapping elements diagonally by leaving the diagnoal ele 
                #not exchanging them
                mat[j][i] , mat[i][j] = mat[i][j], mat[j][i]

    #reverse the matrix, jth col will be 1st cola nd j-1th col will be 2nd col and  so       on
    #we reverse by exchanging the opp end col
    def reverse(self,mat):
        n = len(mat)
        for i in range(n):
            for j in range(n//2):
                #- value of col leads to last col consideration
                mat[i][j] , mat[i][-j -1] = mat[i][-j-1], mat[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reverse(matrix)

        
