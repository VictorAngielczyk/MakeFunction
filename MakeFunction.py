from os import read
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr as pr

xFile = open("x.txt","r")
yFile = open("y.txt","r")

xRaw = xFile.read()
yRaw = yFile.read()

xPoints = xRaw.split(",")
yPoints = yRaw.split(",")

xPointsFloat = [float(xP) for xP in xPoints]
yPointsFloat = [float(yP) for yP in yPoints]

a, b, c, d, e, f= np.polyfit(xPointsFloat,yPointsFloat,5)

print(a,b,c,d,e,f)

fromFunc = []

for i in xPointsFloat:
    fromFunc.append(a*i**5+b*i**4+c*i**3+d*i**2+e*i+f)

corr, _ = pr(fromFunc, yPointsFloat)

print(corr*corr)

plt.plot(xPointsFloat,yPointsFloat,"ro")
plt.plot(xPointsFloat,fromFunc,"ro", color="blue")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

print(fromFunc)
