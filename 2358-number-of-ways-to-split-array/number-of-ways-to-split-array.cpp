class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        long long totalSum=0;
        for(int i=0;i<nums.size();i++){
            totalSum+=nums[i];
        }
        long long left=0;
        long long right=totalSum;
        int count=0;
        for(int i=0;i<nums.size()-1;i++){
            left=left+nums[i];
            right=totalSum-left;
            if(left>=right){
                count++;
            }
        }
        return count;
    }
};