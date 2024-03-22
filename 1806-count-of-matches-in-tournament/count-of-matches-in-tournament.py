class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches=0
        matches = 0
        team_advance = 0
        while n>1:
            matches= n//2
            total_matches+=matches
            team_advance = n-(matches)
            n = team_advance
        return total_matches

        