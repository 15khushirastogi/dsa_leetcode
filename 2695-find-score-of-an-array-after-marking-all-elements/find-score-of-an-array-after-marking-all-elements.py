from heapq import heappush, heappop

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = []
        visited = set()  # To track removed indices
        
        # Push all elements with their indices into the heap
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        
        score = 0
        while heap:
            value, index = heappop(heap)
            
            # Skip if the index is already visited
            if index in visited:
                continue
            
            # Add the value to the score
            score += value
            
            # Mark this index and adjacent ones as visited
            visited.add(index)
            if index > 0:
                visited.add(index - 1)
            if index < n - 1:
                visited.add(index + 1)
        
        return score
