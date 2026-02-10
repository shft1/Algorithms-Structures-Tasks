import bisect
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        l_spells, l_potions = len(spells), len(potions)
        potions.sort()
        for i in range(l_spells):
            idx = bisect.bisect_left(
                potions, success, key=lambda x: x * spells[i]
            )
            spells[i] = l_potions - idx if idx != l_potions else 0
        return spells
