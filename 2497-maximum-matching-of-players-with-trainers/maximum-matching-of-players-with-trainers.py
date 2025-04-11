class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left=0
        right=0
        players_len=len(players)
        trainers_len=len(trainers)
        while(left<players_len and right<trainers_len):
            if(players[left]<=trainers[right]):
                left+=1
                right+=1
            else:
                right+=1


        return left