class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #base condition 
        if grid is None:
            return 0 
        
        rows = len(grid)
        cols = len(grid[0])
        #a visited set to mark all the nodes as visited
        visited =set()
        countIslands =0
        def bfs(r,c):
            #need to maintain a queue and keep updating as and when
            #we go along in bfs so that we can find all the CONNECTED stuff 
            q =collections.deque()       
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row , col = q.popleft()
                direct =[[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in direct:
                    r , c = dr+row, dc + col

                    #while we are continuing to proceed and check next nodes
                    #we must see if its inside boundary and if its 1 
                    if (r in range(rows)) and (c in range(cols)) and (r,c) not in visited and grid[r][c] == "1":
                        q.append((r,c))
                        visited.add((r,c))



        
        #let's start with the traversal of all elements in node
        for r in range(rows):
            for c in range(cols):
                #if we find 1 and it is already not there in visited 
                #then we make bfs call 
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    countIslands +=1 
        
        return countIslands


        
        
