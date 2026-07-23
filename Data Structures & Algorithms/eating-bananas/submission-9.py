class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)

        low, high = 1, max(piles)
        
        while low < high:

            mid = (low + high) // 2

            hours = sum((x + mid - 1) // mid for x in piles)
            
            if hours > h:
                low = mid + 1
            else:
                high = mid

        return low
