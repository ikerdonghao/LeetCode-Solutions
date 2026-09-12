class Solution:
    def isFascinating(self, n: int) -> bool:
        if n > 1000//3:
            return False
        fullStr = str(n)+str(2*n)+str(3*n)
        num_set = []
        for char in fullStr:
            if char in num_set or char == "0":
                return False
            else:
                num_set.append(char)
        return True