import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics


ave = [0]*3
pstdev = [0]*3
val30 = [-1.6944358192475053, -1.5741342207630593, -1.2343582953064827]
val45 = [-1.323380271661203, -1.161679233396521, -1.5327852921065412]
val60 = [-0.9728009386824373, -1.0000001942018806, -0.8371979833825741]


#for plot
degree = [30, 45, 60]

#print(data_1[1][1])

for i in range(3) :
    print(val30[i])

ave[0] = statistics.mean(val30)
ave[1] = statistics.mean(val45)
ave[2] = statistics.mean(val60)

pstdev[0] = statistics.pstdev(val30)
pstdev[1] = statistics.pstdev(val45)
pstdev[2] = statistics.pstdev(val60)
#sum = float(data_1[1][1])

for i in range(3) :
    print(ave[i])

for i in range(3) :
    print(pstdev[i])

fig = plt.figure()
#plot data
plt.plot(degree, ave, color='blue', marker='o', linestyle='-')
#plot error
plt.errorbar(degree, ave, yerr = pstdev, capsize=5, fmt='o', color='blue')


# 体裁を整える
#plt.xlabel("直線部の長さの差(内向き矢羽-外向き矢羽) (矢羽角度30[degree])")
#plt.ylabel("内向き矢羽が長いと答えた確率")

plt.xlabel("Degree of Arrow [degree]")
plt.ylabel("Average of Optical Illusion [degree] \n with error bar (standard deviation)")

plt.ylim(-2.0, -0.8)
plt.xlim(15, 75)
plt.xticks([15, 30, 45, 60, 75])
plt.yticks([-2.0, -1.8, -1.6, -1.4, -1.2, -1, -0.8])
plt.tight_layout()
plt.grid()

# figureの保存
fig_name = "resurt_1-2.png"
plt.savefig(fig_name)

# figureの表示
plt.show()

#print(ave[0])


