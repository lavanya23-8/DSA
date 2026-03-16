class Solution(object):
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                
                sums.add(grid[i][j])

                k = 1
                while i-k >= 0 and i+k < m and j-k >= 0 and j+k < n:
                    total = 0
                  
                    for d in range(k):
                        total += grid[i-k+d][j-d]
                   
                    for d in range(k):
                        total += grid[i+d][j-k+d]
                   
                    for d in range(k):
                        total += grid[i+k-d][j+d]
                    
                    for d in range(k):
                        total += grid[i-d][j+k-d]

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]