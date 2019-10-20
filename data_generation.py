#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:49:52 2019

@author: dan
"""

# Import required packages
import pandas as pd
import numpy as np
import hashlib


# Define a date-range for selection
start = "2019-01-01"
finish = "2019-12-31"

dtRan = pd.date_range(start = start, end = finish)


# Define the categories and probabilities for selection
cats = ["step" + str(x) for x in range(1,5)] 
catProbs = [0.6, 0.25, 0.1, 0.05]


# Generate 1000 range ids
ids = []

for i in range(1, 1001):
    x = hashlib.md5(str(i).encode()).hexdigest()
    ids.append(x)
    

# Create intermediate data set by making 40,000 random selection
sz = 40000
inIds = np.random.choice(ids, sz)
inCts = np.random.choice(cats, sz, p = catProbs)
inDts = np.random.choice(dtRan, sz)

interData = pd.DataFrame({
        "ids": inIds, 
        "category": inCts, 
        "date": inDts})
    

# Group by id and category to the first instance of each 
finalData = (interData.groupby(["ids", "category"])
                      .min()
                      .reset_index())


# Import pickle and dump data 
import pickle

f = open("data.pickle", "wb")
pickle.dump(finalData, f)
f.close()





