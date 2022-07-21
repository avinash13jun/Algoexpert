# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:26:26 2022
@author: Avinash Kumar
"""

"""
1. Tandem bicycle is operated by 2 people
2. Speed is determined by the person pedal faster
3. Find the fastest total speed or slowest based on input

3, 5 -> 5
5, 6 -> 6

6 + 5 -> 11

Fastest :
red -> 2,3,5,5,9
blue -> 7,6,3,2,1

Speed - 7,6,5,5,9 -> 32

Slowest:
red -> 2,3,5,5,9
blue -> 1,2,3,6,7

Speed - 2,3,5,6,9 -> 
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