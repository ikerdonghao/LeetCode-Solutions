class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        if n < 3:
            return arr[n]
        else:
            cur = 3
            while cur <= n:
                arr.append(sum(arr[cur-3:cur]))
                cur += 1
            return arr[n]