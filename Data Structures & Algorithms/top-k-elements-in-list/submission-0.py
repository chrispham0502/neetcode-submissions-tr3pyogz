class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = count.most_common()

        return [sorted_count[i][0] for i in range(k)]
