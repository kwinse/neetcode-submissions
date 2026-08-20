class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        num = x
        while num > 0:
            digit = num%10
            rev = rev*10 + digit
            num //= 10
        return rev == x