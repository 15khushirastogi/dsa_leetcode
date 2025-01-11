class Solution {
public:
    bool canConstruct(string s, int k) {
        int n=s.size();
        if (n < k) return false;

        sort(s.begin(), s.end());
        int oddCount = 0;

        for (int i = 0; i < n; ) {
            char current = s[i];
            int count = 0;
            while (i < n && s[i] == current) {
                count++;
                i++;
            }
            if (count % 2 != 0) oddCount++;
        }

        return oddCount <= k;
    }
};