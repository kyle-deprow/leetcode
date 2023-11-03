from typing import List, Optional

class ListNode:
  def __init__(self, val, next_node=None):
    self.val = val
    self.next = next_node
  
  def __str__(self):
    return '[ListNode val={v}, next={n}]'.format(v=self.val, l=self.next)


# Linked list solution involving 2 pointers where one moves through list
# one at a time and another at twice the speed.  If the list is flat (no
# loops) then the fast pointer will hit a null and return false
# If there is a loop, the fast pointer will eventually look back and equal
# the slow node and return True
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    fast = head
    slow = head

    while fast and fast.next:
      # Move fast pointer two nodes down the list
      fast = fast.next.next
      # Move slow pointer one node on list
      slow = slow.next
      if fast == slow:
        return True
    
    return False