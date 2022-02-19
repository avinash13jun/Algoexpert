# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 07:50:37 2022
@author: Avinash Kumar
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