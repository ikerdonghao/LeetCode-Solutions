class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        n = 1
        for char in order:
            order_map[char] = n
            n+=1
        
        for i in range(len(words)-1):
            prev_word = words [i]
            next_word = words [i+1]
            compare_completed = False
            for j in range(min(len(prev_word),len(next_word))):
                if order_map[prev_word[j]] > order_map[next_word[j]]:
                    return False
                elif order_map[prev_word[j]] < order_map[next_word[j]]:
                    compare_completed = False
                    break
                compare_completed=True
                
            if len(prev_word) > len(next_word) and compare_completed:
                return False
        return True
        
