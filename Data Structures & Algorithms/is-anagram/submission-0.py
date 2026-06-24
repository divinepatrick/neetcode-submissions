class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {char: s.count(char) for char in set(s)}
        frequency_t = {char: t.count(char) for char in set(t)}

        if frequency_s == frequency_t:
            return True
        return False