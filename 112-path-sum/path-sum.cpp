class Solution {
private:
    bool checkSum(TreeNode* root, int targetSum, int curSum) {
        if (root == nullptr) {
            return false;
        }
        
        curSum += root->val;

        if (root->left == nullptr && root->right == nullptr) {
            return curSum == targetSum;
        }

        return checkSum(root->left, targetSum, curSum) || checkSum(root->right, targetSum, curSum);
    }

public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        return checkSum(root, targetSum, 0);
    }
};
