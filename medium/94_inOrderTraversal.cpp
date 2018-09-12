# include <iostream>
# include <vector>
# include <stack>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> output;
        inorderTraversalIterative(root, output);
        // inorderTraversalRecursive(root, output);
        return output;
    }
    
    /*
     * InOrder Traversal is move to left -> root -> right
     * Logic:
     *  - we first move to left child
     *      - keep pushing root and moving to left child till we move to a null child i.e. its parent is a leaf node or only right child
     *      - pop parent and process it                                               ^
     *  - after processing any node, we move on to its right child                    |
     *      - move to right child                                                     |
     *  - if right child is null i.e parent is either a leaf node or no right child---|
     *  - else right child has a left child - move to left child ---------------------|
     */
    void inorderTraversalIterative(TreeNode* root, vector<int> &output)
    {
        stack<TreeNode*> s;
        TreeNode* curr = root;
        // while (!s.empty() || curr)
        while (curr || !s.empty())
        {
            while (curr)
            {
                s.push(curr);
                curr = curr->left;
            }
            curr = s.top();
            s.pop();
            output.push_back(curr->val);
            curr = curr->right;
        } 
    }
    
    /*
     * Trivial
     */
    void inorderTraversalRecursive(TreeNode* root, vector<int> &output)
    {
        if (root)
        {
            if (root->left)
                inorderTraversalRecursive(root->left, output);
                output.push_back(root->val);
            if (root->right)
                inorderTraversalRecursive(root->right, output);
        }
    }
};

int main()
{
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(6);

    Solution* s = new Solution();
    vector<int> res = s->inorderTraversal(root);
    for (int i : res)
        cout << i << " ";
    cout << endl;
    return 0;
}