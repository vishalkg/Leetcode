# include <iostream>
# include <vector>
# include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
    // Using one stack
    vector<int> postorderTraversal(TreeNode* root)
    {
        vector<int> output;
        stack<TreeNode*> s;
        if (root)
        {
            if (root->right)
                s.push(root->right);
            s.push(root);
            root = root->left;
        }
        while (!s.empty())
        {
            if (root)
            {
                if (root->right)
                    s.push(root->right);
                s.push(root);
                root = root->left;
            }
            else
            {
                root = s.top();
                s.pop();
                if (root->right && !s.empty() && root->right==s.top())
                {
                    TreeNode* right = s.top();
                    s.pop();
                    s.push(root);
                    root = right;
                }
                else
                {
                    output.push_back(root->val);
                    root = nullptr;
                }
            }
        }
        return output;
    }
    
    
    // Using two stacks
    /*
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> output;
        // postorderTraversalRecursive(root, output);
        stack<TreeNode*> s1;
        stack<TreeNode*> s2;
        if (root) s1.push(root);
        while (!s1.empty())
        {
            TreeNode* curr = s1.top();
            s1.pop();
            if (curr->left) s1.push(curr->left);
            if (curr->right) s1.push(curr->right);
            s2.push(curr);
        }
        
        while (!s2.empty())
        {
            output.push_back(s2.top()->val);
            s2.pop();
        }
        return output;
    }
    */
    
    // recusrsive soln
    /*
    void postorderTraversalRecursive(TreeNode* root, vector<int> &output)
    {
        if (!root)
            return;
        else
        {
            postorderTraversalHelper(root->left, output);
            postorderTraversalHelper(root->right, output);
            output.push_back(root->val);
        }
    }
    */
};

int main()
{
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    Solution* s = new Solution();
    vector<int> output = s->postorderTraversal(root);
    for (int i=0; i<output.size(); i++)
        cout << output[i] << " ";
    cout << endl;
    return 0;
}