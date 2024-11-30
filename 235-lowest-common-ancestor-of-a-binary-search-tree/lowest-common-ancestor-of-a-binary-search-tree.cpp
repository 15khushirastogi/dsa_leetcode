/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
private:
    void find_path(TreeNode* root, vector<TreeNode*>&visited, TreeNode* node){
        if(root->val==node->val){
            visited.push_back(root);
            return;
        }
        if(node->val<root->val){
            visited.push_back(root);
            find_path(root->left,visited,node);
        }
        else{
            visited.push_back(root);
            find_path(root->right,visited,node);
        }
    }
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*>visited_p;
        vector<TreeNode*>visited_q;
        find_path(root,visited_p,p);
        find_path(root,visited_q,q);
        TreeNode* lca = nullptr;
        for (int i = 0; i < min(visited_p.size(), visited_q.size()); ++i) {
            if (visited_p[i] == visited_q[i]) {
                lca = visited_p[i];
            } else {
                break;
            }
        }
        
        return lca;
    }
};