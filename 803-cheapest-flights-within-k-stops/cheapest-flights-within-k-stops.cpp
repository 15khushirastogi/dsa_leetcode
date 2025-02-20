class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<pair<int,int>>adj[n];
        for(auto it : flights){
            adj[it[0]].push_back({it[1],it[2]});
        }
        vector<int>dist(n,1e9);
        dist[src]=0;
        queue<pair<int,pair<int,int>>>q;
        //{stops,{node,distance}}
        q.push({0,{src,0}});
        while(!q.empty()){
            auto iter=q.front();
            q.pop();
            int stop=iter.first;
            int node=iter.second.first;
            int cost=iter.second.second;

            if(stop>k){
                continue;
            }

            for(auto it: adj[node]){
                int adjNode=it.first;
                int adjCost=it.second;
                if(cost+adjCost<dist[adjNode] && stop<=k){
                    dist[adjNode]=cost+adjCost;
                    q.push({stop+1,{adjNode,cost+adjCost}});
                }
            }
        }
        if(dist[dst]==1e9){
            return -1;
        }
        return dist[dst];
    }
};