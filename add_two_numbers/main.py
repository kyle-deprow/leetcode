from typing import List, Optional
from collections import defaultdict

class ListNode:
  def __init__(self, val, next_node=None):
    self.val = val
    self.next = next_node
  
  def __str__(self):
    return '[ListNode val={v}, next={n}]'.format(v=self.val, l=self.next)

# Since lists are already sorted in reverse order, this is as simple as
# add each digit and carrying over the excess over 10 to the next calculation.
# Create a dummy head to store the resultant list and return the tail of the
# dummy.
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
    dummy_head = ListNode(0)
    tail = dummy_head
    carry_over = 0

    while l1 is not None or l2 is not None or carry_over != 0:
      val1 = l1.val if l1 is not None else 0
      val2 = l2.val if l2 is not None else 0

      sum_val = val1 + val2 + carry_over
      val = sum_val % 10
      carry_over = sum_val // 10

      new_node = ListNode(val)
      tail.next = new_node
      tail = tail.next

      l1 = l1.next if l1 is not None else None
      l2 = l2.next if l2 is not None else None
    
    ans = dummy_head.next
    return ans

if __name__ == '__main__':
  s = Solution()
  test1 = ListNode(1, ListNode(4, ListNode(3)))
  test2 = ListNode(5, ListNode(6, ListNode(4)))
  val = s.addTwoNumbers(test1, test2)
  print(val)