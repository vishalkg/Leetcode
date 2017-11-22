# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    
    if len(lists)==0:
        return []
    if len(lists)==1:
        return lists[0]

    # Approach 1: call mergeKLists recursively to get merged lists for half of lists
    # Call merge2Lists to merge the above two lists
    # Uses the fact that, the two two lists being merged are sorted 
    '''n = len(lists)
    l1 = mergeKLists(lists[0:n//2])
    l2 = mergeKLists(lists[n//2:])
    #print(l1.val,l2.val)
    return merge2Lists(l1,l2)'''

    # However looks, like approach 1 is more expensive , may be due to recursive function call overhead
    # traversal of sorted lists more than one time
    # Approach 2: This is more straight forward
    # Make a list by visiting all the lists and call sort function
    # Straigth forward but doesn't uses the fact that individual lists are sorted
    A = []
    for list in lists:
        while list!=None:
            A.append(list.val)
            list = list.next
    #print(A)
    A.sort()
    return A
    
def merge2Lists(l1,l2):
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