class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        existing_map = {}
        max_gap = -1
        for i in range(len(s)):
            if s[i] not in existing_map.keys():
                existing_map[s[i]] = i
            else:
                gap = i- existing_map[s[i]] -1
                max_gap = max(gap,max_gap)
        return max_gap