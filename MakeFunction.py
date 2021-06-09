import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr as pr

np.set_printoptions(suppress=True)

xFile = open("x.txt","r")
yFile = open("y.txt","r")

xRaw = xFile.read()
yRaw = yFile.read()

xPoints = xRaw.split(",")
yPoints = yRaw.split(",")

xPointsFloat = [float(xP) for xP in xPoints]
yPointsFloat = [float(yP) for yP in yPoints]

z = np.polyfit(xPointsFloat, yPointsFloat, 7)

func = np.poly1d(z)

fromFunc = []

for i in xPointsFloat:
    fromFunc.append(func(i))

corr, _ = pr(fromFunc, yPointsFloat)

print(corr*corr)

plt.plot(xPointsFloat,yPointsFloat, "ro")
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xPointsFloat,func(xPointsFloat))
plt.title("Function")

with open('output.txt', 'a') as file:
    file.truncate()
    file.write('R^2: '+ str(corr*corr))
    file.write('Function: '+ str(func))
    file.close

plt.show()