class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        vector<int> res;
        int n = A.size();
        vector<int> vis(n + 1, 0); 
        int count = 0;

        for (int i = 0; i < n; i++) {
            vis[A[i]]++;
            if (vis[A[i]] == 2) {
                count++; 
            }

            vis[B[i]]++;
            if (vis[B[i]] == 2) {
                count++; 
            }
            
            res.push_back(count);
        }
        return res;
    }
};
