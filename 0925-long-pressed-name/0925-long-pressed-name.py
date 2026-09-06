class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index = 0
        typed_index = 0

        while typed_index < len(typed):
            if name_index < len(name) and name[name_index] == typed[typed_index] :
                print(f"compare {typed_index} of {typed}: {typed[typed_index]} and {name_index} of {name}: {name[name_index]}")
                name_index += 1
                typed_index += 1
            elif typed[typed_index] == name[name_index-1] and typed_index>0:
                typed_index += 1
            else:
                return False
        
        return name_index == len(name)