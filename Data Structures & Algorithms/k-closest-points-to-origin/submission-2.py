class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Finds the k smallest elements based on distance squared
        return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)