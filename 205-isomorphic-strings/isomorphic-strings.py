class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        first_map = []
        second_map = []
        for i in s:
            first_map.append(s.index(i))
        for i in t:
            second_map.append(t.index(i))
        if first_map == second_map:
            return True
        return False