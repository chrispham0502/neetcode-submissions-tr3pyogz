class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            letter = s[i]
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1
            
            letter = t[i]
            if letter in t_count:
                t_count[letter] += 1
            else:
                t_count[letter] = 1

        return s_count == t_count