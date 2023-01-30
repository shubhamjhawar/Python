def solve(board) -> None:
    
    rows = len(board)
    cols = len(board[0])
    if rows <= 2 or cols <= 2:
        return

        #The DFS function to transverse the rows and the columns
    def dfs(i,j,board,rows,cols):
        board[i][j] = '-'
    
        steps = [[-1,0],[1,0],[0,1],[0,-1]]
        for nbr in steps:
            x = i + nbr[0]
            y = j + nbr[1]
            if (x >= 0 and y >= 0 and x < rows and y < cols and board[x][y] == "O"):
                dfs(x,y,board,rows,cols)
            else:
                pass
        

        
    #Visiting the first and the last row
    for j in range(cols):
        if (board[0][j] == "O"):
            dfs(0,j,board,rows,cols)
        if(board[rows-1][j] == "O"):
            dfs(rows-1,j,board,rows,cols)
    
    # visting the first and the last column
    for i in range(rows):
        if (board[i][0] == "O"):
            dfs(i,0,board,rows,cols)
        if(board[i][cols-1] == "O"):
            dfs(i,cols-1,board,rows,cols)
    
    # The 'O' we have not visited are to be conquered and numered as 'X'
    for i in range(rows):
        for j in range(cols):
            if(board[i][j] == 'O'):
                board[i][j] = 'X'
            elif (board[i][j] == '-'):
                board[i][j] = 'O'
                

   
                
    

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
    
    
            
            
        