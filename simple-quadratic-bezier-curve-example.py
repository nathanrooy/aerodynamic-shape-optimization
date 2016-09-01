#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Simple Quadratic Bezier Curve Example
#   2015-08-12
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
import numpy as np

#--- MAIN ---------------------------------------------------------------------+

numPts=20                                   # number of points in Bezier Curve
controlPts=[[0,0],[0.5,1],[1,0]]            # control points
t=np.array([i*1/numPts for i in range(0,numPts+1)])

B_x=(1-t)*((1-t)*controlPts[0][0]+t*controlPts[1][0])+t*((1-t)*controlPts[1][0]+t*controlPts[2][0])
B_y=(1-t)*((1-t)*controlPts[0][1]+t*controlPts[1][1])+t*((1-t)*controlPts[1][1]+t*controlPts[2][1])

#--- PLOT ---------------------------------------------------------------------+

from pylab import *
xPts,yPts=zip(*controlPts)
plot(B_x,B_y,'b',label='Bezier Curve')
plot(xPts,yPts,color='#666666',)
plot(xPts,yPts,'o',mfc='none',mec='r',markersize=8,label='Control Points')
plt.title('Quadratic Bezier Curve')
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,1.1)
plt.legend(loc=1,fontsize=12)
plt.savefig('01-basic-quadratic-bezier-curve.png',dpi=100)
plt.show()

#--- END ----------------------------------------------------------------------+
