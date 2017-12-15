#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

typedef struct ListNode {
    int val;
    ListNode *next;
    //ListNode(int x) : val(x), next(NULL) {}
}ListNode;

/*
* Simple partition the list into two, call sortList on each
* Write a function which merges two linked list
* if head1->val<=head2->val: 
*     result = head; 
*     result->next = merge(head1->next,head2)
* else:
*     //do same as before
* Constant space, 'coz not allocating any extar space, 
* playing in pointers only!
*/


ListNode* sortList(ListNode* head);
ListNode* merge_sortedLList(ListNode* a, ListNode* b);
void split_list(ListNode* source,ListNode* a,ListNode* b);
void printList(ListNode* l);

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head==NULL || head->next==NULL)
            return head;

        ListNode* a = head;
        ListNode* b = head->next;
        while (b!=NULL) {
            b = b->next;
            if (b!=NULL) {
                a = a->next;
                b = b->next;
            }
        }
        b = a->next;
        a->next = NULL;
        a = head;
        printList(a);printList(b);

        a = sortList(a);
        b = sortList(b);
        ListNode* res = merge_sortedLList(a,b);
        //printList(res);
        return (res);

    }

    ListNode* merge_sortedLList(ListNode* a, ListNode* b) {
        ListNode* result = NULL;
        if (a==NULL) 
            return (b);
        else if (b==NULL) 
            return (a);

        if (a->val<=b->val) {
            result = a;
            result->next = merge_sortedLList(a->next,b);
        }
        else {
            result = b;
            result->next = merge_sortedLList(a,b->next);
        }
        return (result);
    }    
};

void printList(ListNode* l) {
    ListNode* temp = l;
    while (l != NULL) {
        cout << l->val << "->";
        l = l->next;
    }
    cout << endl;
}

int main () {
    int x[] = {3,1,2,45,87,9};
    ListNode* head;
    for (int i=0;i<sizeof(x)/sizeof(x[0]);i++) {
        ListNode* new_node = new ListNode;// new ListNode(x[i]);
        new_node->val = x[i];
        new_node->next = head;
        head = new_node;
    }
    printList(head);
    Solution* s = new Solution();
    ListNode* res = s->sortList(head);
    //printList(res);
	return 0;
}



