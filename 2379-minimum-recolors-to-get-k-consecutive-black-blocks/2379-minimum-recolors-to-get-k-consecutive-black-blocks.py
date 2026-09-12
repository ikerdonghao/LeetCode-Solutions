class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = k
        for i in range(len(blocks)-k+1):
            sub_block = blocks[i:i+k]
            print(sub_block)
            print('-'*5)
            op = 0
            for char in sub_block:
                if char == "W":
                    op += 1
            if min_op > op:
                min_op = op
        return min_op
        
