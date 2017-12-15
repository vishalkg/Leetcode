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
* Logic is simple: find linked list of size K
* Reverse it and point the ->next of element to reverseKGroup(remainingList,k)
*/

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head==NULL || head->next==NULL) {
            return (head);
        }
        
        ListNode* p1 = head;
        ListNode* p2 = head;
        int i = 0;
        while (i<k-1) {
            p2 = p2->next;
            if (p2->next==NULL) break;
            else i++;
        }
        if (i<k-2) return head;
        else {
            ListNode* temp = p2->next;
            p2->next = NULL;
            // Reverse list starting p1
            ListNode* prev = NULL;
            ListNode* next;// = NULL;
            ListNode* curr = p1;
            while (curr!=NULL) {
                next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
            head->next = reverseKGroup(temp,k);
            return (prev);
        }
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
    int k = 4;
    ListNode* head;
    for (int i=0;i<sizeof(x)/sizeof(x[0]);i++) {
        ListNode* new_node = new ListNode;// new ListNode(x[i]);
        new_node->val = x[i];
        new_node->next = head;
        head = new_node;
    }
    printList(head);
    Solution* s = new Solution();
    ListNode* res = s->reverseKGroup(head,k);
    printList(res);
    return 0;
}