class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        if (nums.empty()) return 0;

        int incCount = 1, decCount = 1, maxLength = 1;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]) {
                incCount++; 
                decCount = 1; 
            } 
            else if (nums[i] < nums[i - 1]) {
                decCount++;  
                incCount = 1; 
            } 
            else {
                incCount = 1; 
                decCount = 1;
            }

            maxLength = max(maxLength, max(incCount, decCount));
        }

        return maxLength;
    }
};
