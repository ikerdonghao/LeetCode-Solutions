# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not (isBadVersion(n-1)):
            return n
        
        i=n // 2
        gap = n//2
        while True: 
            if isBadVersion(1):
                return 1
            print("i is "+str(i)+", gap is "+ str(gap))
            if not isBadVersion(i) and isBadVersion(i+1):
                return i+1
            if isBadVersion(i) and isBadVersion(i+1): # Both bad version, look to earlier
                i = i - gap // 2
                gap = gap // 2 + 1
            if not isBadVersion(i) and not isBadVersion(i+1): # Both good version, look later
                i = i + gap // 2
                gap = gap // 2 + 1
            print("-"*5)