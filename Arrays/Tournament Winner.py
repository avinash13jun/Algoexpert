# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 06:24:31 2022

@author: Avinash Kumar
"""

def tournamentWinner(competitions, results):
    winners = {}
    def addWinner(program):
        if program in winners.keys():
            winners[program] += 1
        else:
            winners[program] = 1
            
    for i in range(len(results)):
        homeTeamWin = True if results[i] == 1 else False
        if homeTeamWin:
            addWinner(competitions[i][0])
        else:
            addWinner(competitions[i][1])
    
    return max(winners, key = winners.get)
			



competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
scores = [0, 0, 1]
result = tournamentWinner(competitions, scores)
print(result)