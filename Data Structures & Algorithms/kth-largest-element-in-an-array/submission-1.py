class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # create max heap
        heapq.heapify_max(nums)

        for _ in range(k):
            res = heapq.heappop_max(nums)
        
        return res