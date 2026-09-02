class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        for num in arr:
            if num == 0:
                continue
            if num % 2 == 0 and arr.count(num//2) > 0:
                return True
        return False