from math import sqrt
import numpy as np
from numpy import cos, deg2rad, sin, deg2rad


def forwardQ_TRPY(ztrans, ytrans, xtrans, roll, pitch, yaw):
    '''
    Takes in z,y,x trasnlation coordinates and roll,pitch,yaw data in degrees.
    '''
    roll_rad = deg2rad(roll)
    pitch_rad = deg2rad(pitch)
    yaw_rad = deg2rad(yaw)

    return np.array([[cos(roll_rad)*cos(pitch_rad),
                      cos(roll_rad)*sin(pitch_rad)*sin(yaw_rad)-sin(roll_rad)*cos(yaw_rad),
                      cos(roll_rad)*sin(pitch_rad)*cos(yaw_rad)+sin(roll_rad)*sin(yaw_rad),
                      xtrans],
                     
                     [sin(roll_rad)*cos(pitch_rad),
                      sin(roll_rad)*sin(pitch_rad)*sin(yaw_rad)+cos(roll_rad)*cos(yaw_rad),
                      sin(roll_rad)*sin(pitch_rad)*cos(yaw_rad)-cos(roll_rad)*sin(yaw_rad),
                      ytrans],
                     
                     [-sin(pitch_rad),
                      cos(pitch_rad)*sin(yaw_rad),
                      cos(pitch_rad)*cos(yaw_rad),
                      ztrans],
                     
                     [0, 0, 0, 1]])

Q10 = forwardQ_TRPY(-10,40,15,45,-30,0)

Q31 = np.array([[-1/2,-1/2,sqrt(2)/2,40],
               [1/2,1/2,sqrt(2)/2,200],
               [-sqrt(2)/2,sqrt(2)/2,0,-20],
               [0,0,0,1]])

Q21 = forwardQ_TRPY(-50,25,10,-15,70,-60)

Q23 = forwardQ_TRPY(20,-5,40,90,-10,45)

pA_r3 = np.array([[6],
                  [5],
                  [-3],
                  [1]])

pB_r1 = np.array([[-6],
                  [4],
                  [2],
                  [1]])

print(Q23 @ np.linalg.inv(Q21) @ pB_r1)