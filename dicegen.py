# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:06:18 2021

@author: pmjum
"""

import random

def fourDsixSim(numTrials):
    total = 0
    for x in range(numTrials):
        nums = []
        for y in range(4):
            nums.append(random.randint(1,6))
        nums.remove(min(nums))
        total += sum(nums)
    return total/numTrials

def diceGen(numTrials,diceType,numDice,numDropped):
    total = 0
    for x in range(numTrials):
        nums = []
        for y in range(numDice):
            nums.append(random.randint(1,diceType))
        if(numDropped > 0):
            for z in range(numDropped):
                nums.remove(min(nums))
        total += sum(nums)
    return total/numTrials