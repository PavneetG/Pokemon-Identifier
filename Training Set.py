#!/usr/bin/env python
# coding: utf-8
import numpy 
from pprint import pprint
import tensorflow

def extract_data(inputFile):
    stats = []
    pokemonTypeLabels = []

    with open(inputFile) as file:
        items = file.readlines()
    
    title = items[1]
    data = items[1:]
    
    for item in data:
        row = item.split(',')
        pokemon = []
        element = []
        pokemon.append(str(row[1]))
        element.append(str(row[2]))
        elementlist = ["Grass","Fire", "Water", "Bug", "Normal", "Poison","Electric", "Ground", "Psychic", "Fighting", "Ghost", "Ice", "Rock", "Dragon", "Fairy", "Steel", "Dark", "Flying"]
        stat = []
        for i in range(5,12):
            stat.append(row[i])
        stats.append(stat); 
        pokemonTypeLabels.append(elementlist.index(element[0]))
    
    return stats, pokemonTypeLabels, elementlist

def typeID(ID,elementList):
    return elementlist[ID]


def generateValidationSet(data,ratio = 0.1):
    length = len(data)
    numValidation = int(length*ratio)
    IDs = range (length)
    
    validationDataIDs = random.sample(IDs, numValidation)
    trainingDataIDs = list(set(IDs)-set(numValidation))
    
    return trainingDataIDs, validationDataIDs

