class Solution {
private:
    bool checkPath(TreeNode* root, int targetSum, vector<int>& path) {
        if (root == nullptr) {
            return false;
        }
        path.push_back(root->val);

        if (root->left == nullptr && root->right == nullptr) {
            int pathSum = 0;
            for (int val : path) {
                pathSum += val;
            }
            if (pathSum == targetSum) {
                return true;
            }
        }

        bool leftCheck = checkPath(root->left, targetSum, path);
        bool rightCheck = checkPath(root->right, targetSum, path);

        path.pop_back();

        return leftCheck || rightCheck;
    }

public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        return checkPath(root, targetSum, path);
    }
};
