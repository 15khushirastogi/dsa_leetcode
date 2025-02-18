class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rows=matrix.size();
        int cols=matrix[0].size();

        queue<pair<int,int>>q;
        //find all the occurence of zeros
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==0){
                    q.push({i,j});
                }
            }
        }
        while(!q.empty()){
            int r=q.front().first;
            int c=q.front().second;
            q.pop();
            //update rows
            for(int i=0;i<rows;i++){
                matrix[i][c]=0;
            }
            //update columns
            for(int j=0;j<cols;j++){
                matrix[r][j]=0;
            }
        }
    }
};