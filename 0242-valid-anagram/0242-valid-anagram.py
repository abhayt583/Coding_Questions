class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            
        if len(s) != len(t):
            return False

        char_counts = {}

        for i in range(len(s)):
            char_counts[s[i]] = char_counts.get(s[i], 0) + 1
            char_counts[t[i]] = char_counts.get(t[i], 0) - 1

        for count in char_counts.values():
            if count != 0:
                return False

        return True