class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1 = 0
        index2 = 0
        min_common = -1
        while index1 < len(nums1) and index2<len(nums2):
            if nums1[index1] == nums2[index2]:
                min_common = nums1[index1]
                break
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                index1 += 1
        return min_common