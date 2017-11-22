# Recursive Approach
# 1st get p2.next using recursive approach
# Adjust p1, p2
# Assign p2 to head
# return head
# Beats 100% of python submissions on Leetcode

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head==None:
        return None
    if head.next==None:
        return head
    p1 = head
    p2 = p1.next
    p2.next = self.swapPairs(head.next.next)
    p1.next = p2.next
    p2.next = p1
    head = p2
    return head