class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        maxlen = 0

        for num in nums:
            if (num-1) not in numset: # is start of a sequence
                seq = 0
                while num in numset:
                    seq += 1
                    num += 1

                maxlen = max(seq, maxlen)
        
        return maxlen