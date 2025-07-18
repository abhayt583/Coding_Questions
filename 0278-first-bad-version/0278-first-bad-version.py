# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s=1
        while s<n:
            mid = s + (n - s) // 2
            if (isBadVersion(mid)):
                n=mid
            else:
                s=mid+1
        return s
            

        