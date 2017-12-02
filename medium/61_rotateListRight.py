# Rotate linked list 
# Catch, if length(list)<k, then k = k%length(list)
# Rest is straight forward

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return head
    temp,count = head, 0
    while temp != None:
        temp, count = temp.next, count+1
    k = k%count
    p2 = head
    while k>0:
        p2 = p2.next
        if p2==None: return head
        k -= 1
    p1 = head
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    p2.next = head
    head = p1.next
    p1.next = None
    return head