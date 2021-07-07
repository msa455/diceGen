# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:06:18 2021

@author: pmjum
"""

import random
import matplotlib.pyplot as plt

def fourDsixSim(numTrials):
    total = 0
    for x in range(numTrials):
        nums = []
        for y in range(4):
            nums.append(random.randint(1,6))
        nums.remove(min(nums))
        total += sum(nums)
    return total/numTrials

def diceGen(numTrials,diceType,numDice,numDropped,summed=True):
    avgs = []
    for x in range(numTrials):
        nums = []
        for y in range(numDice):
            nums.append(random.randint(1,diceType))
        if(numDropped > 0):
            for z in range(numDropped):
                nums.remove(min(nums))
        avgs.append(sum(nums))
    if(summed):
        return sum(avgs)/len(avgs)
    else:
        return avgs


def diceStats(numRolls,diceType,numDice,numDropped):
    nums = []
    for x in range(numRolls):
        rolls = []
        for y in range(numDice):
            rolls.append(random.randint(1,diceType))
        if(numDropped > 0):
            for z in range(numDropped):
                rolls.remove(min(rolls))
        nums.append(sum(rolls))
    nums.sort()
    counts = {}
    for num in nums:
        if(num in counts):
            counts[num]+=1
        else:
            counts[num] = 1
    return(counts)
    

def displayRolls(numRolls,diceType,numDice,numDropped):
    data = diceStats(numRolls,diceType,numDice,numDropped)
    names = list(data.keys())
    values = list(data.values())
    
    plt.bar(range(len(names)), values, tick_label=names)
    plt.show()

print(diceGen(10000,6,3,0))
displayRolls(100000,6,3,0)
