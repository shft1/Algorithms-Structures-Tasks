from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senateL = len(senate)
        queueR, queueD = deque(), deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                queueR.append(i)
            else:
                queueD.append(i)
        cntR, cntD = len(queueR), len(queueD)
        while cntR != 0 and cntD != 0:
            ri, di = queueR.popleft(), queueD.popleft()
            if ri < di:
                queueR.append(ri + senateL)
                cntD -= 1
            else:
                queueD.append(di + senateL)
                cntR -= 1
        return "Radiant" if cntD == 0 else "Dire"
