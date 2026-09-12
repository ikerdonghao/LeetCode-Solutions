class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"        
        }
        pending_list = []
        for symbol in s:
            # print("Current symbol is: " + symbol)
            # print("pending is "+pending)
            if symbol in mapping:
                if pending_list:
                    last_pending = pending_list.pop()
                else:
                     return False
                if mapping[symbol] != last_pending:
                    return False
            else:
                pending_list.append(symbol)
        return not pending_list