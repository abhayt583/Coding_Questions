class Solution:
    def validPalindrome(self, s: str) -> bool:
        s=list(s)

        one=0
        two=len(s)-1
        while one<two:
            if s[one]!=s[two]:
                two=two-1
                if s[one]!=s[two]:
                    two=two+1
                    one=one+1
                    if s[one]!=s[two]:
                        return False
            else:
                two-=1
                one+=1
        return True

        