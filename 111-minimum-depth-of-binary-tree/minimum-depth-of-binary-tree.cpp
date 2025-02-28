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
    int minDepth(TreeNode* root) {
        if(root==nullptr){
            return 0;
        }
        int ans=1e9;
        // {node,count}
        queue<pair<TreeNode*,int>>q;
        q.push({root,1});
        while(!q.empty()){
            int size=q.size();
            int count=q.front().second;
            for(int i=0;i<size;i++){
                TreeNode* node=q.front().first;
                q.pop();
                if(node->left){
                    q.push({node->left,count+1});
                }
                if(node->right){
                    q.push({node->right,count+1});
                }
                if(node->left==nullptr && node->right==nullptr){
                    ans=min(ans,count);
                }
            }
        }
        return ans;
    }
};