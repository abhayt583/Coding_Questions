class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=1
        while n*n<=num:
            if n*n==num:
                return True
            n+=1
        return False
        