def solve(board) -> None:

    rows = len(board)
    cols = len(board[0])
    if rows <= 2 or cols <= 2:
        return

    #The DFS function to transverse the rows and the columns
    def dfs(i,j,visited,board,rows,cols):
        visited[i][j] = 1
    
        steps = [[-1,0],[1,0],[0,1],[0,-1]]
        for nbr in steps:
            x = i + nbr[0]
            y = j + nbr[1]
            if (x >= 0 and y >= 0 and x < rows and y < cols and visited[x][y] == 0 and board[x][y] == "O"):
                dfs(x,y,visited,board,rows,cols)
            else:
                pass
    

    #Created Visited Array for the keeping track of the 'O' we visited from the boundary
    visited=[[0 for j in range(cols)] for i in range(rows)]
    

    #Visiting the first and the last row
    for j in range(cols):
        if (board[0][j] == "O"):
            dfs(0,j,visited,board,rows,cols)
        if(board[rows-1][j] == "O"):
            dfs(rows-1,j,visited,board,rows,cols)
    
    # visting the first and the last column
    for i in range(rows):
        if (board[i][0] == "O"):
            dfs(i,0,visited,board,rows,cols)
        if(board[i][cols-1] == "O"):
            dfs(i,cols-1,visited,board,rows,cols)
    
    # The 'O' we have not visited are to be conquered and numered as 'X'
    for i in range(rows):
        for j in range(cols):
            if(visited[i][j] == 0 and board[i][j] == 'O'):
                board[i][j] = 'X'
    

if __name__ == '__main__':
   
          
    mat = [ [ 'X', 'O', 'X', 'O', 'X', 'X' ],
            [ 'X', 'O', 'X', 'X', 'O', 'X' ],
            [ 'X', 'X', 'X', 'O', 'X', 'X' ],
            [ 'O', 'X', 'X', 'X', 'X', 'X' ],
            [ 'X', 'X', 'X', 'O', 'X', 'O' ],
            [ 'O', 'O', 'X', 'O', 'O', 'O' ]];
    
    solve(mat)
 
    for i in range(6):
        print(*mat[i])
    
    
            
            
        