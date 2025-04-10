class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1): 
            return s
        dp = ['']*numRows 
        i=0
        direction = -1
        for char in s:
            dp[i]+=char 
            if(i==0 or i==numRows-1): 
                direction *= -1
            i += direction 
        return ''.join(dp)