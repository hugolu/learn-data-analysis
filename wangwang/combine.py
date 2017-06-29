#!/usr/bin/env python

import numpy as np
import pandas as pd
import os
from os import path

if path.isfile('all.csv'):
    os.remove('all.csv')

data = pd.concat([pd.read_csv(f) for f in os.listdir('.') if f.endswith('.csv')])
del data['Unnamed: 6']
data.to_csv('all.csv')
