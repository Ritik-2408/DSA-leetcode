class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        a = x
        b = 0

        while x > 0:
            c = x % 10
            b= b * 10 + c
            x = x // 10
            
        return a == b