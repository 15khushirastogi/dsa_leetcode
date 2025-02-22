class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        int z=x+y;
        vector<int>vis(z+1,0);
        queue<int>q;
        q.push(0);
        vis[0]=1;
        int steps[]={-x,+x,-y,+y};
        while(!q.empty()){
            int node=q.front();
            q.pop();
            if(node==target){
                return true;
            }
            for(int i=0;i<4;i++){
                int newnode=node+steps[i];
                if(newnode>=0 && newnode<=z && vis[newnode]==0){
                    q.push(newnode);
                    vis[newnode]=1;
                }
            }
        }
        return false;
    }
};