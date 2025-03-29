class Solution:
    def reverseWords(self, s: str) -> str:
        #s=s.strip()
        print(s)
        words = s.split()
        print(words)
        reversed_words = words[::-1]
        print(reversed_words)
        
       
        result = " ".join(reversed_words)
        
        return result