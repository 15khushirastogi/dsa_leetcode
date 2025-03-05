class Solution {
private:
    int tri(int n, vector<int>& dp) {
        if (dp[n] != -1) return dp[n]; 
        dp[n] = tri(n - 1, dp) + tri(n - 2, dp) + tri(n - 3, dp); 
        return dp[n];
    }

public:
    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;

        vector<int> dp(n + 1, -1);
        dp[0] = 0, dp[1] = 1, dp[2] = 1;
        return tri(n, dp);
    }
};
