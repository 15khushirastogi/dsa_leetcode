/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
      queue<TreeNode*>q;
      if(root==nullptr){
        return nullptr;
      }
      q.push(root);
      while(!q.empty()){
        TreeNode* node=q.front();
        q.pop();
        if(node->left){
            q.push(node->left);
        }
        if(node->right){
            q.push(node->right);
        }
        if(node->left || node->right){
            TreeNode* leftval=node->left;
            node->left=node->right;
            node->right=leftval;
        }

      } 
      return root; 
    }
};