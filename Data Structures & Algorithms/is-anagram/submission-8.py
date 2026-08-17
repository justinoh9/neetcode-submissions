class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lwk can't I cheese this quesiton by using sorted()
        return sorted(s) == sorted(t)