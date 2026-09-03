class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cumulative = 0
        result_list = []
        for i in nums:
            cumulative = cumulative*2 + i
            if cumulative % 5 == 0:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list