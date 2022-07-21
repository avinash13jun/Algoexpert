# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:26:26 2022
@author: Avinash Kumar
"""

"""
Class Photos:
    1. Seperate students wearing red shirt and blue shirt (Equal students)
    2. Students in red shirt should be in same row and blue shirt in same row
    3. Students in back row must be taller than students in front of them
"""

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    isRedFront = redShirtHeights[0] < blueShirtHeights[0]
    
    for i in range(len(redShirtHeights)):
        if isRedFront:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    return True

redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
res = classPhotos(redShirtHeights, blueShirtHeights)
print(res)

