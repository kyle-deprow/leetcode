from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __str__(self):
    return '[TreeNode val={v}, left={l}, right={r}]'.format(v=self.val, l=self.left, r=self.right)

# utilizing the fact that in-order traversal of a Binary Search Tree
# guarantees sorted sequence of values.  Equivalent values will appear
# as repeated integers which we can count and track.  If we find multiple
# values with the same mode characteristic, return array with all repeating
# values
class Solution:
  def __init__(self):
    self.current_count = 0
    self.current_val = 0
    self.max_count = 0
    self.modes = []

  def in_order_traversal(self, node: Optional[TreeNode]):
    if not node:
      return
    # In-order traversal starts on the left sub-tree
    self.in_order_traversal(node.left)
    self.current_count = self.current_count + 1 if node.val == self.current_val else 1
    self.current_val = node.val

    # Replace mode value with current value becuase we've now seen it more than
    # any other value
    if self.current_count > self.max_count:
      self.max_count = self.current_count
      self.modes = [node.val]
    # Current mode val ties previous highest val repetition, append to return
    elif self.current_count == self.max_count:
      self.modes.append(node.val)
    
    # In-order traversal ends on the left sub-tree
    self.in_order_traversal(node.right)

  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    self.in_order_traversal(root)
    return self.modes

if __name__ == '__main__':
  s = Solution()
  test_tree = TreeNode(val=1, right=TreeNode(val=2, right=TreeNode(val=2)))
  val = s.findMode(test_tree)
  print(val)