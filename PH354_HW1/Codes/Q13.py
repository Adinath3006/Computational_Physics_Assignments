""" Exercise 13 """

# Part A

import matplotlib.pyplot as plt

month = []
sunspot_num = []

file = open('sunspots.txt','r')
for line in file:
    lines = [float(i) for i in line.split()]
    month.append(lines[0])
    sunspot_num.append(lines[1])

plt.plot(month,sunspot_num)
plt.xlabel('Month')
plt.ylabel('Sunspot Number')
plt.title("Observed number of sunspots on the Sun")
plt.savefig("Q13_a.png")
plt.show()

# Part B

plt.plot(month[0:1000],sunspot_num[0:1000])
plt.xlabel('Month')
plt.ylabel('Sunspot Number')
plt.title("Observed number of sunspots on the Sun for the first 1000 months")
plt.savefig("Q13_b.png")
plt.show()

# Part C

Running_Avg = []

for j in range(0,990):
    sum = 0
    for k in range(0,10):
        sum += sunspot_num[j+k]
    Running_Avg.append(sum/10)

plt.plot(month[0:1000],sunspot_num[0:1000],label = 'Original Data')
plt.plot(month[4:994],Running_Avg, color='black', label = 'Running Average')
plt.xlabel('Month')
plt.ylabel('Sunspot Number')
plt.title("Observed number of sunspots on the Sun for the first 1000 months")
plt.savefig("Q13_c.png")
plt.legend()
plt.show()