class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def parseString(string):
            char_list = []
            freq_list = []
            index = 0
            for char in string:
                if index > 0:
                    if char == char_list[index-1]:
                        freq_list[index-1] += 1
                        continue
                    else:
                        char_list.append(char)
                        freq_list.append(1)
                        index += 1
                        continue
                else:
                    char_list.append(char)
                    freq_list.append(1)
                    index += 1
                    continue

            return {"char_list":char_list ,
                "freq_list":freq_list }

        name_map = parseString(name)
        type_map = parseString(typed)

        print(f"name_map is {name_map}")
        print(f"type_map is {type_map}")
        print(f"freq_diff is {[y-x for x,y in zip(name_map["freq_list"],type_map["freq_list"])]}")
        if name_map["char_list"] != type_map["char_list"]:
            return False
        elif min([y-x for x,y in zip(name_map["freq_list"],type_map["freq_list"])]) < 0:
            return False
        else:
            return True
