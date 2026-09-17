class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        cur_index = 0
        count = 0
        prev_r_edge = -1
        while cur_index < 2*n-1:
            l = cur_index // 2
            r = l + (cur_index % 2)
            print(f"cur_index = {cur_index},l={l},r={r}")
            while l >= 0 and r < n and s[l] == s[r]:
                if l <= prev_r_edge:
                    break
                print(f"checking {s[l:r+1]}")
                sub_len = r-l+1
                if sub_len >=k:
                # if l <= prev_r_edge or r > n-1 or s[l] != s[r]:
                    count += 1
                    prev_r_edge = r
                    cur_index = 2 * r - 1
                    print(f"new prev edge = {prev_r_edge}")
                l-=1
                r+=1
            cur_index += 1
        return count