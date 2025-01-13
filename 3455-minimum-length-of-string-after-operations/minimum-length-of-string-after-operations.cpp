class Solution {
public:
    int minimumLength(string s) {
        int n=s.size();
        if(n<3){
            return n;
        }
        int ans=0;
        unordered_map<char,int>freq;
        for(int i=0;i<n;i++){
            if(freq.find(s[i])==freq.end()){
                freq[s[i]]=1;
            }
            else{
                freq[s[i]]++;
            }
        }
        for (auto it : freq) {
            if (it.second % 2 == 0) {
                ans += 2;
            } else {
                ans += 1;
            }
        }
        return ans;
    }
};