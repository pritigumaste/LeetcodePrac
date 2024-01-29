#Time: O(m*n) 
# number of rows * number of col
#space: O(n) 
#space for queues and visited set

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

      
        curr = image[sr][sc]
        if color == curr:
            return image
        rows = len(image)
        cols = len(image[0])
        visited= set()

        def bfs(r,c, color):
            q= collections.deque()
            q.append((r,c))
            visited.add((r,c))
            
            direct =[[1,0], [0,1], [-1,0], [0,-1]]
            while q:
                rr,cc =q.popleft() 
                image[rr][cc] = color
                for dr, dc in direct:
                    row, col = rr+dr, cc+dc
                    print(row,col)
                    if (row, col) not in visited and (row in range(rows)) and (col in range(cols)) and image[row][col] == curr:
                    # if (row, col) not in visited and (0 <= row < rows) and (0 <= col < cols) and image[row][col] == curr:
                        print("inside",row, col)
                        
                        
                        print(image)
                        q.append((row,col))
                        visited.add((row,col))
      
        #no need of this because anyhow we are itertaing through all the indexes frm
        #above using direction
        # for r in range(rows):
        #     for c in range(cols):
        #         if r == sr and c == sc:
        #             image[r][c] =color
        bfs(sr,sc, color)
        return image
        
