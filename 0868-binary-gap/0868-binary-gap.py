class Solution:
    def binaryGap(self, n: int) -> int:
        string = f"{n:b}"
        if int(string[::-1]) == 1:
            return 0
        while string[-1] == "0":
            string = string[:-1]
        separated_set = set(string.split("1"))
        print(f"set is {separated_set}")
        max_length = 0
        while separated_set:
            ele_length = len(separated_set.pop())
            max_length = ele_length if ele_length>max_length else max_length
        return max_length+1