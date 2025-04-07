class Solution {
private:
    int prev = -1; 
    void dfs(TreeNode* root, int &mindiff){
        if(root == nullptr) return;

        dfs(root->left, mindiff);

        if(prev != -1) {
            mindiff = min(mindiff, abs(root->val - prev));
        }
        prev = root->val;

        dfs(root->right, mindiff);
    }

public:
    int minDiffInBST(TreeNode* root) {
        int mindiff = INT_MAX;
        dfs(root, mindiff);
        return mindiff;
    }
};
