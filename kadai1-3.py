import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics
import scipy
import scipy.stats

sum_s = [0]*11
ave = [0]*3
pstdev = [0]*11
s_b = 0.0
s_w = 0.0
s_t = 0.0

#for plot
x = [[0 for i in range(3)] for j in range(3)]
val30 = [-1.6944358192475053, -1.5741342207630593, -1.2343582953064827]
val45 = [-1.323380271661203, -1.161679233396521, -1.5327852921065412]
val60 = [-0.9728009386824373, -1.0000001942018806, -0.8371979833825741]

ave[0]  = statistics.mean(val30)
ave[1]  = statistics.mean(val45)
ave[2]  = statistics.mean(val60)
ave = statistics.mean([ave[0], ave[1], ave[2]])

print('p_value')

p_value = scipy.stats.f_oneway(val30, val45, val60)

print(p_value.pvalue)


