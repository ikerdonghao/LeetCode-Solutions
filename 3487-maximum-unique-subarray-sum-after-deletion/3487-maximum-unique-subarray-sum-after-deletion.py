class Solution:
    def maxSum(self, nums: List[int]) -> int:
        non_neg = [x for x in set(nums) if x >= 0]
        if not non_neg:
            return max(nums)
        return sum(non_neg)