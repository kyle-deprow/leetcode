from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Typical Depth First Search implementation. Recursively call max depth
# and return depth when execution hits terminal leafs
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
      if not root: return depth
      return max(dfs(root.left, depth+1), dfs(root.right, depth+1))

    return dfs(root, 0)

if __name__ == '__main__':
  s = Solution()
  test_tree = TreeNode(val=3, left=TreeNode(val=9), right=(TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))))
  val = s.maxDepth(test_tree)
  print(val)