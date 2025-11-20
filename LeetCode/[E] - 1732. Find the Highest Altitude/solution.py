class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        mxAlt, curr = 0, 0
        for i in range(len(gain)):
            curr += gain[i]
            if curr > mxAlt:
                mxAlt = curr
        return mxAlt
