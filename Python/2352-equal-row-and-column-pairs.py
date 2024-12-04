from collections import defaultdict

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Count the number of instances where a column is equal to a row
        
        count = 0

        # Defaultdict super helpful to automatically fill with 0
        hashMap = defaultdict(int)
        
        # Fill hashmap with rows and occurrences
        for row in grid:
            row = str(row)
            hashMap[row] += 1
        
        # Check columns against hashmap, and add associated count
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[0])):
                col.append(grid[j][i])
            print(col)
            col = str(col)
            count += hashMap[col]
        
        return count