class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        self.min_m = m
        self.min_n = n
        for op in ops:
            op_m = op[0]
            op_n = op[1]
            if (op_m == m and op_n == n):
                continue
            if (op_m == 0 or op_n == 0):
                continue
            if op_m < self.min_m:
                self.min_m = op_m
            if op_n < self.min_n:
                self.min_n = op_n
        return self.min_m * self.min_n

            