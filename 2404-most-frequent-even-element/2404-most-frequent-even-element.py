class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_map = {}
        max_freq = 0
        for num in nums:
            if num % 2 == 0:
                if num in even_map:
                    even_map[num] += 1
                else:
                    even_map[num] = 1
        if not(even_map):
            return -1
        max_freq = max(even_map.values())
        max_freq_candidate = [number for number,freq in even_map.items() if freq==max_freq]
        return min(max_freq_candidate)