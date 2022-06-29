#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:28:32 2022

@author: jonny
"""
import os

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


os.chdir('/home/jonny/Documents/nhs/IS_ucl')
test = pd.read_csv("test_dir.csv")
snmd = pd.read_csv("map.csv")

print(test.head())

map_id = dict(zip(test.clinical_indication, test.Test_ID))

print(map_id)

snmd["test_id"] = snmd["origional"].map(map_id)

print(snmd.head())

snmd.to_csv("test.csv")
