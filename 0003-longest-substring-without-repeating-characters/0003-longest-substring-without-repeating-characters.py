class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary={}
        start=0
        end=0
        for i,char in enumerate(s):
            if char in dictionary and start<=dictionary[char]:
                start=dictionary[char]+1
            else:
                end=max(end,i-start+1)
            dictionary[char]=i
        return end
        