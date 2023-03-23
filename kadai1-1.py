import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics


sum_s = [0]*11
ave = [0]*11
pstdev = [0]*11

#for plot
x = [0]*11


#データ読み出し
with open('data/degree_60/MullerLyer_KI_001_pf.csv') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data_1 = [row for row in reader]


with open('data/degree_60/MullerLyer_KI_002_pf.csv') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data_2 = [row for row in reader]

with open('data/degree_60/MullerLyer_KI_003_pf.csv') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data_3 = [row for row in reader]

print('data_1')

for i in data_1 :
    print(i)

print('data_2')
for i in data_2 :
    print(i)

print('data_3')
for i in data_3 :
    print(i)

#print(data_1[1][1])

for i in range(0, 11) :
    sum_s[i] = data_1[i][1] + data_2[i][1] + data_3[i][1]
    ave[i] = statistics.mean([data_1[i][1], data_2[i][1], data_3[i][1]])
    pstdev[i] = statistics.pstdev([data_1[i][1], data_2[i][1], data_3[i][1]])
    x[i] = data_1[i][0]
#sum = float(data_1[1][1])

for i in range(11) :
    print(ave[i])

for i in range(11) :
    print(pstdev[i])



fig = plt.figure()
#plot data
plt.plot(x, ave, color='blue', marker='o', linestyle='-')
#plot error
plt.errorbar(x, ave, yerr = pstdev, capsize=5, fmt='o', color='blue')


# 体裁を整える
#plt.xlabel("直線部の長さの差(内向き矢羽-外向き矢羽) (矢羽角度30[degree])")
#plt.ylabel("内向き矢羽が長いと答えた確率")

plt.xlabel("Inward - Outward length (Degree = 60[degree])")
plt.ylabel("Average of Prob. (inward is longer) \n with error bar (standard deviation)")

plt.ylim(-0.25,1.25)
plt.xlim(min(x)-0.5, max(x)+0.5)
plt.xticks([-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1,  1.5, 2, 2.5])
plt.yticks([-0.25, 0, 0.25, 0.5, 0.75, 1, 1.25])
plt.tight_layout()
plt.grid()

# figureの保存
fig_name = "resurt_60.png"
plt.savefig(fig_name)

# figureの表示
plt.show()

#print(ave[0])


