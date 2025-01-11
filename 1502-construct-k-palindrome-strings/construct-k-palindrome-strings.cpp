class Solution {
public:
    bool canConstruct(string s, int k) {
        int n=s.size();
        if(n<k){
            return false;
        }
        if(n==k){
            return true;
        }
        int freq[26]={0};
        for(int i=0;i<n;i++){
            char ch=s[i];
            int ind=ch-'a';
            freq[ind]++;
        }
        int count=0;
        for(int i=0;i<26;i++){
            if(freq[i]%2!=0){
                count++;
            }
        }
        return count<=k;
    }
};