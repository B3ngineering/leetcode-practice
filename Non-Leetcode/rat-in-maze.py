from typing import List

class Solution:

    def solve(self, i, j, a, n, ans, move, visited, di, dj):
        # If we are at the destination, add the current path to the answer list
        if i == n-1 and j == n - 1:
            ans.append(move)
            return
        
        # Define the directions in the order Down, Left, Right, Up
        dir = "DLRU"

        # Explore all four possible directions
        for index in range(4):
            nexti = i + di[index]
            nextj = j + dj[index]
            # Check if the next move is within the grid, not visited, and is a valid path
            if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not visited[nexti][nextj] and a[nexti][nextj] == 1:
                # Mark the current cell as visited
                visited[i][j] = 1
                # Recursively explore the next cell
                self.solve(nexti, nextj, a, n, ans, move + dir[index], visited, di, dj)
                # Unmark the current cell
                visited[i][j] = 0
                

    def findPath(self, m, n) -> List[str]:
        ans = []
        # Generate an empty list of lists
        visited = [[0 for j in range(n)] for i in range(n)]

        # Define directions
        di = [+1, 0, 0, -1]
        dj = [0, -1, 1, 0]

        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", visited, di, dj)
        return ans




if __name__ == '__main__':
    n = 4
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    obj = Solution()
    result = obj.findPath(m, n)
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")
    print()