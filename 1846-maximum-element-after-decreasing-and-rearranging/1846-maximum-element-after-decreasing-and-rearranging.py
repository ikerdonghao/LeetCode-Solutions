class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # ops = 1
        arr.sort()
        if len(arr) == 1:
            return 1
        for i in range(len(arr)-1):
            if i==0:
                if arr[0] > 1:
                    arr[0] = 1
                    # ops += 1
                continue
            if arr[i] - arr[i-1] > 1:
                arr[i] = min(arr[i-1]+1,arr[i+1]-1)
                # ops += 1
        if arr[-1] - arr[-2] > 1:
            arr[-1] = arr[-2] + 1
            # ops += 1
        print(arr)
        return max(arr)

            