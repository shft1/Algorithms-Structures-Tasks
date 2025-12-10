package main

func predictPartyVictory(senate string) string {
	senateL := len(senate)
	queueR, queueD := make([]int, 0), make([]int, 0)
	for i := 0; i < senateL; i++ {
		if senate[i] == 'R' {
			queueR = append(queueR, i)
		} else {
			queueD = append(queueD, i)
		}
	}
	cntR, cntD := len(queueR), len(queueD)
	for cntR != 0 && cntD != 0 {
		ri, di := queueR[0], queueD[0]
		if ri < di {
			queueR = append(queueR, ri+senateL)
			cntD--
		} else {
			queueD = append(queueD, di+senateL)
			cntR--
		}
		queueR, queueD = queueR[1:], queueD[1:]
	}
	if cntR == 0 {
		return "Dire"
	}
	return "Radiant"
}
