class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_map = {}
        for index,num in enumerate(nums):
            compliment = target - num

            if compliment in checked_map:
                return [checked_map[compliment],index]
            else:
                checked_map[num]=index
        return []