import os
import sys
import json
import math
import numpy as np
#import matplotlib.pyplot as plt 
from scipy.special import erfc

fn = os.path.join(os.path.dirname(__file__), 'previous_data/ackermann.json')
with open(fn, 'rb') as f:
    original = json.load(f)

data = []
for time in original:
    data += original[time]

x = np.sort(data)

x = np.unique(x)

def get_relatived_value(arr, rel_idx):
    forward_bias, idx = math.modf(rel_idx * len(arr))
    if idx+1 == len(arr):
        return arr[-1]
    first_bias = 1 - forward_bias
    v1 = np.array(arr[int(idx)]) * first_bias
    v2 = np.array(arr[int(idx)+1]) * forward_bias
    return (v1 + v2).tolist()

epsilon = 1e-9
def denormalize(value):
    if value >= 1:
        value = 1-epsilon
    if value <= 0:
        value = epsilon
    return get_relatived_value(x, value)
