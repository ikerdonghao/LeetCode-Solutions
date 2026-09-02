class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        groups = (s).split("0")
        print(f"groups is {groups}")
        return len(groups) - groups.count("") == 1