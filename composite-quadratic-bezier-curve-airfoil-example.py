#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Composite Quadratic Bezier Curve Example (Airfoil)
#   2015-08-12
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
import numpy as np

#--- MAIN ---------------------------------------------------------------------+

def quadraticBezier(t,points):
    B_x=(1-t)*((1-t)*points[0][0]+t*points[1][0])+t*((1-t)*points[1][0]+t*points[2][0])
    B_y=(1-t)*((1-t)*points[0][1]+t*points[1][1])+t*((1-t)*points[1][1]+t*points[2][1])
    return B_x,B_y

def airfoil(ctlPts,numPts,write):
    curve=[]
    t=np.array([i*1/numPts for i in range(0,numPts)])
    
    # calculate first Bezier curve
    midX=(ctlPts[1][0]+ctlPts[2][0])/2
    midY=(ctlPts[1][1]+ctlPts[2][1])/2
    B_x,B_y=quadraticBezier(t,[ctlPts[0],ctlPts[1],[midX,midY]])
    curve=curve+zip(B_x,B_y)

    # calculate middle Bezier Curves
    for i in range(1,len(ctlPts)-3):
        p0=ctlPts[i]
        p1=ctlPts[i+1]
        p2=ctlPts[i+2]
        midX_1=(ctlPts[i][0]+ctlPts[i+1][0])/2
        midY_1=(ctlPts[i][1]+ctlPts[i+1][1])/2
        midX_2=(ctlPts[i+1][0]+ctlPts[i+2][0])/2
        midY_2=(ctlPts[i+1][1]+ctlPts[i+2][1])/2

        B_x,B_y=quadraticBezier(t,[[midX_1,midY_1],ctlPts[i+1],[midX_2,midY_2]])
        curve=curve+zip(B_x,B_y)                      
   
    # calculate last Bezier curve
    midX=(ctlPts[-3][0]+ctlPts[-2][0])/2
    midY=(ctlPts[-3][1]+ctlPts[-2][1])/2

    B_x,B_y=quadraticBezier(t,[[midX,midY],ctlPts[-2],ctlPts[-1]])
    curve=curve+zip(B_x,B_y)
    curve.append(ctlPts[-1])

    # write airfoil coordinates to text file
    if write:
        xPts,yPts=zip(*curve)
        f=open('airfoilCoords.txt','wa')
        for i in range(len(xPts)):
            f.write(str(xPts[i])+','+str(yPts[i])+'\n')
        f.close()

    return curve

#--- 11 CONTROL POINT AIRFOIL EXAMPLE -----------------------------------------+

points=[[1,0.001],              # trailing edge (top)
        [0.76,0.08],
        [0.52,0.125],
        [0.25,0.12],
        [0.1,0.08],
        [0,0.03],               # leading edge (top)
        [0,-0.03],              # leading edge (bottom)
        [0.15,-0.08],
        [0.37,-0.01],
        [0.69,0.04],
        [1,-0.001]]             # trailing edge (bottom)

#--- RUN EXAMPLE --------------------------------------------------------------+

curve=airfoil(points,16,write=True) # pick even number of points so that the leading edge is defined by a single point...

#--- PLOT ---------------------------------------------------------------------+

from pylab import *
import matplotlib.pyplot as plt

xPts,yPts=zip(*points)
xPts2,yPts2=zip(*curve)
plot(xPts2,yPts2,'b')
plot(xPts,yPts,color='#666666')
plot(xPts,yPts,'o',mfc='none',mec='r',markersize=8)
plt.title('Composite Quadratic Bezier Curve Based Airfoil')
plt.xlim(-0.05,1.05)
plt.ylim(-0.55,0.55)
##plt.savefig('airfoil-final.png',dpi=72)
plt.show()

#--- END ----------------------------------------------------------------------+
