class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        long long count = 0;
        
        for (int i = 0; i < nums.size(); ++i) {
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Find the smallest j such that nums[i] + nums[j] >= lower
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (nums[i] + nums[mid] >= lower) right = mid - 1;
                else left = mid + 1;
            }
            int start = left;

            left = i + 1;
            right = nums.size() - 1;
            
            // Find the largest j such that nums[i] + nums[j] <= upper
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (nums[i] + nums[mid] <= upper) left = mid + 1;
                else right = mid - 1;
            }
            int end = right;
            
            // Add to count the number of valid pairs with i as the first element
            if (start <= end) {
                count += end - start + 1;
            }
        }
        
        return count;
    }
};
