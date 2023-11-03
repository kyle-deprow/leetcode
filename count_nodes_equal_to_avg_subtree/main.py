from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __str__(self):
    return '[TreeNode val={v}, left={l}, right={r}]'.format(v=self.val, l=self.left, r=self.right)

# Solution involves understanding the nuance in tree-traversal strategies, but at the core understands
# that at each subtree we gather the average of the current subtree and compare to the node's val.
# If we choose pre/in order traversal strategies, there will be many re-traversals of trees (O(n^2))
# post-order traversal guarantees that we only need to go through tree once.
# From here, we only need to gather the sum and size of each tree and perform the avg calculation at
# each node.  If equal, add one to the overall output and move up the tree.
class Solution:
  avg_count = 0

  def post_order_traversal(self, root: Optional[TreeNode]):
    if not root:
      return (0,0)
    
    lsum, lcount = self.post_order_traversal(root.left)
    rsum, rcount = self.post_order_traversal(root.right)

    cur_sum = lsum + rsum + root.val
    cur_count = lcount + rcount + 1

    if cur_sum // cur_count == root.val:
      self.avg_count += 1

    return (cur_sum, cur_count)

  def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    self.post_order_traversal(root)
    return self.avg_count