class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        path = set() # Keeps a path of all the tuples in order to not have any repeating locations

        def dfs(r, c, i):
            if i == len(word):
                return True

                
            # Makes sure r and c are bound to the board also makes sure that the ith letter of word
            # matches the current location on the board and finally checks if we have explored a location 
            # before 
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or word[i] != board[r][c] or (r,c) in path:
                return False
            
            #Recursively tracks all paths until correct one is found returns true
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c-1,i+1))
            path.remove((r,c))
            return res

        #Finds the starting point for word within the array
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False