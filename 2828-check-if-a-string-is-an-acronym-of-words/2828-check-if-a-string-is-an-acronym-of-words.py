class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        from_array = ''
        for word in words:
            from_array = from_array + word[0]
        if from_array == s:
            return True
        else: return False