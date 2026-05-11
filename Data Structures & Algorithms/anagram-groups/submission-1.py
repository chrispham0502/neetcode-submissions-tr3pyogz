class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) # [k, v] is [freq, list of anagram]

        for s in strs:
            count = Counter(s)
            key = tuple(sorted(count.items()))
            res[key].append(s)

        return list(res.values())