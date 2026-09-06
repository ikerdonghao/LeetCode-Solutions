class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_map = {}
        for char in arr:
            if char not in freq_map:
                freq_map[char] = 1
            else:
                freq_map[char] += 1
        filtered_map = {key:value for key,value in freq_map.items() if value == 1}
        print(filtered_map)
        if len(filtered_map) < k:
            return ""
        else:
            # print(list(filtered_map.keys())[k-1])
            return list(filtered_map.keys())[k-1]