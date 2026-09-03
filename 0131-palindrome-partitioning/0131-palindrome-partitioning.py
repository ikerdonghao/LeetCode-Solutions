class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(string:str):
            return string == string[::-1]
        if len(s) == 0:
            return [[]]

        ans = []
        for i in range(len(s)):
            left_part = s[0:i+1]
            if isPalin(left_part):
                right_part = self.partition(s[i+1:])
                for p in right_part:
                    ans.append([left_part] + p)
        return ans