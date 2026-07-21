class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []

        # O(n)
        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            dist.append([d, [x, y]])

        # O(n)
        heapq.heapify(dist)

        res = []
        for _ in range(k):
            d, point = heapq.heappop(dist)
            res.append(point)


        return res