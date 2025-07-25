class Solution:
    def validPalindrome(self, s: str) -> bool:
        one = 0
        two = len(s) - 1

        while one < two:
            if s[one] != s[two]:
                # Check by skipping left or right
                left_skip = s[one+1:two+1]
                right_skip = s[one:two]
                return left_skip == left_skip[::-1] or right_skip == right_skip[::-1]
            one += 1
            two -= 1
        return True
