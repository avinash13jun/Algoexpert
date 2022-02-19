# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 07:50:37 2022
@author: Avinash Kumar
"""

def minimumWaitingTime(queries):
    queries.sort()
    if len(queries) < 2:
        return 0
    waitingTime = 0
    totalTime = 0
    for i, q in enumerate(queries):
        if i == 0:
            continue
        waitingTime += queries[i-1]
        totalTime += waitingTime
        
    return totalTime

queries = [3, 2, 1, 2, 6]
res = minimumWaitingTime(queries)
print(res)