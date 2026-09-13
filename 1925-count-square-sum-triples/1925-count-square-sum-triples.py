class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n):
            j = i+1
            k = i+2
            while k <= n:
                k = math.sqrt(i**2+j**2)
                if k.is_integer() and k <= n:
                    print(f"i:{i},j:{j},k:{k},")
                    count +=2
                j += 1
        return count