class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        output = ""
        iterate = 1
        while (iterate -1) * 2 * k < len(s):
            if 2*k*iterate > len(s):
                subStr = s[(iterate -1) * 2 * k:]                
            else:
                subStr = s[(iterate -1) * 2 * k:iterate * 2 * k]
            print(f"sub string is {subStr}")

            if len(subStr) > k:
                addStr = subStr[0:k][::-1] + subStr[k:]
            else:
                addStr = subStr[::-1]
            
            iterate+=1
            output+=addStr
        return output