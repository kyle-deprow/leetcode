from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Typical Depth First Search implementation with comparison.
# Recursively call tree leaves and return comparison checks
# between the two trees
class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def dfc(p, q):
      if not p and not q: return True
      elif not p or not q or (p.val != q.val): return False
      return (p.val == q.val) & dfc(p.right, q.right) & dfc(p.left, q.left)

    return dfc(p, q)

if __name__ == '__main__':
  s = Solution()
  test_tree = TreeNode(val=3, left=TreeNode(val=9), right=(TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))))
  val = s.maxDepth(test_tree)
  print(val)