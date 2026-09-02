class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_map = {}
        for num in arr1:
            if num not in arr1_map:
                arr1_map[num] = 1
            else:
                arr1_map[num] += 1
        output = []
        for num in arr2:
            while arr1_map[num] > 0:
                output.append(num)
                arr1_map[num] -= 1
        sorted_dict = dict(sorted(arr1_map.items()))
        for key,item in sorted_dict.items():
            if item < 1:
                continue
            else:
                while arr1_map[key] > 0:
                    output.append(key)
                    arr1_map[key] -= 1
        return output