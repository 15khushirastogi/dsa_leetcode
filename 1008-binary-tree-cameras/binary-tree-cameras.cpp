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
private:
    int count=0;
    
    int dfs(TreeNode* node){
        
        if(node==nullptr){
            return 1;
        }
        int lc=dfs(node->left);
        int rc=dfs(node->right);
        if(lc==-1 || rc==-1){
            count++;
            return 0;
        }
        if(lc==0 || rc==0){
            return 1;
        }
        return -1;
    }
public:
    int minCameraCover(TreeNode* root) {
        if(dfs(root)==-1){
            count++;
        }
        return count;
    }
};