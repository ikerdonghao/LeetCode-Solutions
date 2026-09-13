class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = -1
        if min(nums) < k:
            return ops
        unique_num = set(nums)
        return len([x for x in unique_num if x > k])