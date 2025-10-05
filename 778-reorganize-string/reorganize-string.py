import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        #creating a hashmap to count the frequencies
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        # insert all the frequency count in the priority queue
        pq=[]
        for key,value in freq.items():
            heapq.heappush(pq,(-value,key))

        for val in freq.values():
            if val>(n+1)//2:
                return ""
        result=[]
        prev_count=0
        prev_ch=""
        while pq:
            count,ch=heapq.heappop(pq)
            result.append(ch)
            if prev_count<0:
                heapq.heappush(pq,(prev_count,prev_ch))

            prev_count,prev_ch=count+1,ch

        rearranged=""
        if len(result)>n:
            return result
        return "".join(result)


        

        