class Solution {
private:
    bool isUnivalued(TreeNode* root, int value){
        if (root == nullptr) {
            return true;
        }
        if (root->val != value) {
            return false;
        }
        return isUnivalued(root->left, value) && isUnivalued(root->right, value);
    }

public:
    bool isUnivalTree(TreeNode* root) {
        if (root == nullptr) return true; 
        return isUnivalued(root, root->val);
    }
};
