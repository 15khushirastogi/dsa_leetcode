class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> st(wordList.begin(), wordList.end());
        if (st.find(endWord) == st.end()) return 0;
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        st.erase(beginWord); 

        while (!q.empty()) {
            string word = q.front().first;
            int steps = q.front().second;
            q.pop();

            for (int i = 0; i < word.size(); i++) {
                char originalChar = word[i]; 

                for (char ch = 'a'; ch <= 'z'; ch++) {
                    word[i] = ch;

                    if (word == endWord) return steps + 1;

                    if (st.find(word) != st.end()) {
                        st.erase(word);
                        q.push({word, steps + 1});
                    }
                }

                word[i] = originalChar; 
            }
        }

        return 0; 
    }
};