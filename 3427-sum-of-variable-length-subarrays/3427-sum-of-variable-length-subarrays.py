class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        accumulate = 0
        for i in range(len(nums)):
            if i-nums[i]<0:
                print(nums[0:i+1])
                print('a--')
                accumulate += sum(nums[0:i+1])
            else:
                accumulate += sum(nums[i-nums[i]:i+1])
                print(nums[i-nums[i]:i+1])
                print('b--')
        return accumulate