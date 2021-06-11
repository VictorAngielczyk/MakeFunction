import os
import glob
import math
import imageio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import pearsonr as pr

now = datetime.now()

files = glob.glob('pics/*')
for f in files:
    os.remove(f)

xFile = open("stuff/x.txt","r")
yFile = open("stuff/y.txt","r")

xRaw = xFile.read()
yRaw = yFile.read()

xPoints = xRaw.split(",")
yPoints = yRaw.split(",")

xPointsFloat = [float(xP) for xP in xPoints]
yPointsFloat = [float(yP) for yP in yPoints]

matplotlib.rcParams['toolbar'] = 'None'
plt.show(block=False)

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

for i in range(1,15):

    z = np.polyfit(xPointsFloat, yPointsFloat, i)

    func = np.poly1d(z)

    fromFunc = []

    for j in xPointsFloat:
        fromFunc.append(func(j))

    corr, _ = pr(fromFunc, yPointsFloat)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(color='gray', linestyle='-', linewidth=1)
    plt.xlim(int(min(xPointsFloat))+0.5,int(max(xPointsFloat))+0.5)
    plt.ylim(0,max(yPointsFloat)+0.5)
    plt.plot(xPointsFloat,yPointsFloat, "ro")
    plt.plot(xPointsFloat,func(xPointsFloat))
    plt.title("r²: " + str(corr*corr) + " n: " + str(i))
    plt.text(0, 5, "Polynomial Function of " + ordinal(i) + " degree", fontsize=14)
    plt.savefig("pics/"+str(i))
    plt.pause(0.1)
    plt.clf()

np.set_printoptions(suppress=True)

with open('output.txt', 'a') as file:
    file.truncate()
    file.write('R^2: '+ str(corr*corr))
    file.write('Function: '+ str(func))
    file.close()

antiDeriv = (math.pi*func**2).integ()

print(antiDeriv(float(max(xPointsFloat)))-antiDeriv(float(min(xPointsFloat))))

images = []

index = 1

while True:

    filename = 'pics/'+str(index)+'.png'

    if os.path.exists(filename):

        images.append(imageio.imread(filename))
        images.append(imageio.imread(filename))
        images.append(imageio.imread(filename))

        index += 1
    
    else:

        break

dt_string = now.strftime("%H_%M_%S")

imageio.mimsave('gifs/'+dt_string+'.gif', images)