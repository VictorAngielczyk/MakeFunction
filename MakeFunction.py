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

a, b, c, d, e, f, g, h= np.polyfit(xPointsFloat,yPointsFloat,7)

print(a,b,c,d,e,f,g,h)

fromFunc = []

for i in xPointsFloat:
    fromFunc.append(a*i**7+b*i**6+c*i**5+d*i**4+e*i**3+f*i**2+g*i+h)

corr, _ = pr(fromFunc, yPointsFloat)

print(corr)

plt.plot(xPointsFloat,yPointsFloat,"ro")
plt.plot(xPointsFloat,fromFunc,"ro", color="blue")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

print(fromFunc)
