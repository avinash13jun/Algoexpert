# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 07:50:37 2022
@author: Avinash Kumar
"""

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    
    if fastest:
        blueShirtSpeeds.sort(reverse = True)
    
    speed = 0
            
    for idx in range(len(blueShirtSpeeds)):
        speed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
    return speed

redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True
res = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
print(res)