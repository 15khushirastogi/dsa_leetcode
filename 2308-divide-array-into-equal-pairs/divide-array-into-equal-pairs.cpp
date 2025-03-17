class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]]++;
        }

        for(int j=0;j<mp.size();j++){
            if(mp[j]%2!=0){
                return false;
            }
        }
        return true;
    }
};