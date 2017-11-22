# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Approach 1: Gather all the elements and call sort
    # k = m+n
    # Time complexity = O(k logk)
    """
    A = []
    while l1!=None:
        A.append(l1.val)
        l1 = l1.next
    while l2!=None:
        A.append(l2.val)
        l2 = l2.next
    A.sort()
    return A
    """
    
    # Approach 2: traverse both the lists simultaneously
    # Time complexity: O(m+n)
    if l1==None or l2==None:
        return l2 if l1==None else l1
    l3 = None
    if l1.val<=l2.val:
        l3 = ListNode(l1.val)
        l1 = l1.next
    else:
        l3 = ListNode(l2.val)
        l2 = l2.next
    result = l3
    while True:
        if l1==None or l2==None:
            if l1==None:
                l3.next = l2
            else:
                l3.next = l1
            break
        else:
            #print(l3.val,l1.val,l2.val)
            temp = None
            if l1.val<=l2.val:
                temp = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            l3.next = temp
            l3 = l3.next
    return result
    