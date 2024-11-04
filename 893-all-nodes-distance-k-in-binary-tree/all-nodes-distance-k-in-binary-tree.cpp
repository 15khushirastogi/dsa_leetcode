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
    void markparent(TreeNode* root,unordered_map<TreeNode*,TreeNode*>&parenttrack){
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            TreeNode* current=q.front();
            q.pop();
            if(current->left){
                parenttrack[current->left]=current;
                q.push(current->left);
            }
            if(current->right){
                parenttrack[current->right]=current;
                q.push(current->right);
            }
        }
    }
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_map<TreeNode*,TreeNode*>parenttrack;
        markparent(root,parenttrack);
        unordered_map<TreeNode*,bool>visited;
        queue<TreeNode*>q;
        q.push(target);
        visited[target]=true;
        int distance=0;
        while(!q.empty()){
            int size=q.size();
            if(distance==k){
                break;
            }
            distance++;
            for(int i=0;i<size;i++){
                TreeNode* current=q.front();
                q.pop();
                if(current->left && !visited[current->left]){
                    visited[current->left]=true;
                    q.push(current->left);
                }
                if(current->right && !visited[current->right]){
                    visited[current->right]=true;
                    q.push(current->right);
                }
                if(parenttrack[current] && !visited[parenttrack[current]]){
                    q.push(parenttrack[current]);
                    visited[parenttrack[current]]=true;
                }
            }
        }
        vector<int>ans;
        while(!q.empty()){
            ans.push_back(q.front()->val);
            q.pop();
        }
        return ans;
    }
};