class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
       vector<int>result;
       int n=nums.size();
       for (int i = 0; i <= n - k; ++i) {
            bool isSorted = true;
            int max_val = nums[i];

            for (int j = i; j < i + k - 1; ++j) {
                if (nums[j+1] != nums[j]+1) {
                    isSorted = false;  
                    break;
                }
                max_val = max(max_val, nums[j + 1]);  
            }

            if (isSorted) {
                result.push_back(max_val);  
            } else {
                result.push_back(-1);  
            }
        }

       return result;
    }
};