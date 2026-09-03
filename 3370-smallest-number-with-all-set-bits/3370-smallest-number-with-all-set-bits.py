class Solution:
    def smallestNumber(self, n: int) -> int:
        output = 1
        # if n==1:
        #     return 1 
        # else:
        while output <= n:
            output *= 2
        return output-1