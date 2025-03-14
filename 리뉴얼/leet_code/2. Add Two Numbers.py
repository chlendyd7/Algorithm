# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        # Base Case: If both lists are empty and carry is 0, return None
        if not l1 and not l2 and carry == 0:
            return None
        
        # Get values of the current nodes, defaulting to 0 if node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Compute sum and next carry
        total = val1 + val2 + carry
        carry = total // 10  # Carry for the next step
        
        # Create the new node with the ones place of the sum
        result_node = ListNode(total % 10)
        
        # Recursively process the next nodes
        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        result_node.next = self.addTwoNumbers(next_l1, next_l2, carry)
        
        return result_node  # Return the head of the computed linked list
