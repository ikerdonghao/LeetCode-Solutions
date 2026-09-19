class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digi_count = [0] * 10
        ans = 0
        for i in digits:
            digi_count[i]+=1
        print(digi_count)
        
        for num in range(100,1000,2):
            a,b,c = num//100, (num//10)%10, (num%10)
            remain = [x for x in digi_count]
            remain[a] = remain[a] - 1
            remain[b] = remain[b] - 1
            remain[c] = remain[c] - 1
            if min(remain) >= 0:
                ans += 1
        return ans