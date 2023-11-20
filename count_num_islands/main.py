from typing import List, Optional

# Solution involves a DFS search over a 2D array.
# Start by iterating at 0,0 and either move horizontal
# or vertical.  When encountering a 1 (land), replace with
# # character to signify evaluation.  Then perform a DFS
# from this coordinate in all adjacent directions to find
# connecting land segments.  After replacing all adjacent
# land with #, increment count and continue search for other
# islands.
class Solution:
  def numIslands(self, grid: Optional[List[List[str]]]) -> int:
    if not grid:
      return 0
    ans = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          self.dfs(grid, i, j)
          ans += 1
    return ans

  def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
    if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) or grid[i][j] != '1':
      return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)

if __name__ == '__main__':
  s = Solution()
  test = [\
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
    ]
  print(s.numIslands(test))