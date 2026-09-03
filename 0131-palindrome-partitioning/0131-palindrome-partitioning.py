class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalin(string: str) -> bool:
            return string == string[::-1]

        def backtrack(start_index: int, path: List[str]):
           
            if start_index == len(s):
                res.append(path[:])  
                return
            
            for i in range(start_index, len(s)):
                left_part = s[start_index : i+1]
                if isPalin(left_part):
                    path.append(left_part)              
                    backtrack(i + 1, path)            
                    path.pop()                          

        backtrack(0, [])
        return res