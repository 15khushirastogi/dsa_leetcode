class Solution {
private:
    int f(vector<int>& arr){
        int prev=arr[0];
        int prev2=0;
        int n=arr.size();
        for(int i=1;i<n;i++){
            int rob=arr[i];
            if(i>1){
                rob+=prev2;
            }
            int notrob=0+prev;

            int cur=max(rob,notrob);

            prev2=prev;
            prev=cur;

        }
        return prev;
    }
public:
    int rob(vector<int>& nums) {
        vector<int>temp1,temp2;
        int n=nums.size();
        if(n==1){
            return nums[0];
        }
        for(int i=0;i<n;i++){
            if(i!=0){
                temp1.push_back(nums[i]);
            }
            if(i!=n-1){
                temp2.push_back(nums[i]);
            }
        }
        return max(f(temp1),f(temp2));
    }
};