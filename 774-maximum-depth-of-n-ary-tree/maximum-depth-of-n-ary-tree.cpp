/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    int maxDepth(Node* root) {
        if(root==nullptr){
            return 0;
        }
        int maxlevel=0;
        queue<pair<Node*,int>>q;
        q.push({root,1});
        while(!q.empty()){
            Node* node=q.front().first;
            int level=q.front().second;
            q.pop();
            maxlevel=max(maxlevel,level);
            for(auto child: node->children){
                q.push({child,level+1});
            }
        }
        return maxlevel;
    }
};