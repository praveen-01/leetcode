class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for res in accounts:
            maxi=max(maxi,sum(res))
        return maxi
        