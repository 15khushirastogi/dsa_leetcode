class Solution1 {
public:
    int fib(int n) {
        if(n==0)
        {
            return 0;
        }
        if(n==1)
        {
            return 1;
        }
        else
        {
            return fib(n-1)+fib(n-2);
        }
    }
};

class Solution2 {
public:
    int fib(int n) {
        if(n==0){
            return 0;
        }
        if(n==1)
        {
            return 1;
        }
        int a=0;
        int b=1;
        int c;
        for(int i=2;i<=n;i++)
        {
            c=a+b;
            a=b;
            b=c;
        }
        return c;
    }
};

class Solution {
private:
    int f(int n,vector<int>&dp){
        if(n<=1){
            return n;
        }
        //check for the subproblem in the dp
        if(dp[n]!=-1){
            return dp[n];
        }
        //now solve for subproblems and store them in dp
        dp[n]=f(n-1,dp)+f(n-2,dp);
        return dp[n];
    }
public:
    int fib(int n) {
        //declaring dp array
        vector<int>dp(n+1,-1);
        return f(n,dp);
    }
};