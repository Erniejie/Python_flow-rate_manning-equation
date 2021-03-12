
# FLOW RATE in a TRAPEZOIDAL CHANNEL_Manning Equation- Civil Engineering
# dr Ron Eaglin_YIJIE

import math

#Global Parameters:

Q = 0.6   # flow rate of design [m^3/s]
a= 0.025  # n: value depending of the surface roughness of channel
b = 0.63     # b: width bottom of channel [m]
c=1.5        #z: side slope
d=0.001    #s: channel bed slope [m/m]
e = 1   

def TrapezoidalQ(n,b,y,z,s):
    A = b*y +z*y*y   # area
    W = b+ 2*y*math.sqrt(1+ z*z)  # wet perimeter
    R = A/W                       # hydraulic radius
    #Q =1.49/n*(A*math.pow(R,2/3)*math.sqrt(s))# Imperial Units
    Q =1/n*(A*math.pow(R,2/3)*math.sqrt(s))# SI (Metric System)
    return Q
print(TrapezoidalQ(a,b,0.63,c,d))

def CalculateDepth(Q,n,b,z,s):
    """set initial values for error accuracy and increment)"""
    error = 1
    accuracy=0.001
    increment = 0.1
    ys=1

    while (error >accuracy):
        print(error,accuracy)
        qa=TrapezoidalQ(n,b,ys,z,s)
        erro = Q - qa

        if (error >0):
            ys = ys + increment

        else:
            ys = ys - increment
            increment =increment/2
            error = -error
        return ys
