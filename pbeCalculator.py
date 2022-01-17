import math
import random
import sys
import statistics

def calcPBE(score):
	cost = score - 8
	if(score >= 14):
		cost += score - 13
	if(score >= 16):
		cost += score - 15
	return cost
	return score - 8 + (0,score-13)[score>13] + (0,score-15)[score>15]
	if score < 14:
		return score - 8
	elif score < 16:
		return (score - 8) + (score - 13)
	else:
		return (score - 8) + (score - 13) + (score - 15)
scores = []
PBEs = []
for j in range(0,1000001):
	PBE = 0
	for i in range(0,6):
		die1 = random.randint(1,6)
		min = die1
		die2 = random.randint(1,6)
		if die2 < min:
			min = die2
		die3 = random.randint(1,6)
		if die3 < min:
			min = die3
		die4 = random.randint(1,6)
		if die4 < min:
			min = die4
		#scores.append(die1 + die2 + die3 + die4 - min)
		PBE += calcPBE(die1 + die2 + die3 + die4 - min)
	PBEs.append(PBE)
	if j%100000 == 0:
		print(j,':',statistics.mean(PBEs))
print('done')
