class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        n=(len(x_str))
        for i in range(n//2):
            if x_str[i] != x_str[n-1-i]:
                return False
        return True