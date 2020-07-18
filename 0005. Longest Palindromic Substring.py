from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_boundaries(left, right, str):
            while left >= 0 and right < len(str) and str[left] == str[right]:
                left -= 1
                right += 1

            return left+1, right-1

        n = len(s)
        ans = ''

        for i in range(n):
            first_left, first_right = palindrome_boundaries(i, i, s)

            if first_right - first_left + 1 > len(ans):
                ans = s[first_left:first_right+1]

            if i+1 < n:
                second_left, second_right = palindrome_boundaries(i, i+1, s)

                if second_right - second_left + 1 > len(ans):
                    ans = s[second_left:second_right+1]

        return ans
