class Solution(object):
    def numberOfSubmatrices(self, grid):
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        # 2D arrays to store prefix data
        # Adding an extra row/col initialized to 0 helps avoid out-of-bounds checks for i-1 or j-1
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        x_count = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                val = 1 if grid[i][j] == 'X' else (-1 if grid[i][j] == 'Y' else 0)
                is_x = 1 if grid[i][j] == 'X' else 0
                
                prefix_sum[i+1][j+1] = val + prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j]
                
            
                x_count[i+1][j+1] = is_x + x_count[i][j+1] + x_count[i+1][j] - x_count[i][j]
       
                if prefix_sum[i+1][j+1] == 0 and x_count[i+1][j+1] > 0:
                    ans += 1
                    
        return ans