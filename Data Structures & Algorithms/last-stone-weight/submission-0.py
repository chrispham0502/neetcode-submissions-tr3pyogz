class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while (len(stones) > 1):
            larger = heapq.heappop_max(stones)
            smaller = heapq.heappop_max(stones)

            remain = larger - smaller

            if remain > 0:
                heapq.heappush_max(stones, remain)

        if stones:
            return stones.pop()

        return 0