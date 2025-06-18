class Solution:
    def reverseVowels(self, s: str) -> str:
        one=0
        two=len(s)-1
        ss=list(s)
        while one<two:
            if ss[one] not in "aeiouAEIOU":
                one=one+1
            elif ss[two] not in "aeiouAEIOU":
                two=two-1
            else:
                ss[one],ss[two]=ss[two],ss[one]
                one=one+1
                two=two-1
        return ''.join(ss)

        