class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []

        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            dist.append([d, [x, y]])

        dist.sort()

        return [point for d, point in dist[:k]]