from math import sqrt
import numpy as np
from numpy import cos, deg2rad, sin, deg2rad


def forwardQ_TRPY(ztrans, ytrans, xtrans, roll, pitch, yaw):
    '''
    Takes in z,y,x trasnlation coordinates and roll,pitch,yaw data in degrees and calculates the forward composed
    transformation using the TRPY convention.
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

def A_matrix (l, d, alpha, theta):
    '''
    Calculates the A matrix given the following Denavit-Hartenburg parameters:
    l = distance between Zi and Zi+1
    d = distance between Xi and Xi+1
    alpha = angle between Zi and Zi+1
    theta = angle between Xi and Xi+1
    '''
    alpha_rad = deg2rad(alpha)
    theta_rad = deg2rad(theta)

    return np.array([[(cos(theta_rad)),
                      -sin(theta_rad)*cos(alpha_rad),
                      sin(theta_rad)*sin(alpha_rad),
                      l*cos(theta_rad)],
                     
                     [(sin(theta_rad)),
                      cos(theta_rad)*cos(alpha_rad),
                      -cos(theta_rad)*sin(alpha_rad),
                      l*sin(theta_rad)],
                     
                     [0,
                      sin(alpha_rad),
                      cos(alpha_rad),
                      d],
                     
                     [0, 0, 0, 1]])

## A matrices
a1 = A_matrix(50,60,0,30)
a2 = A_matrix(0,0,180,45)
a3 = A_matrix(0,50,0,0)
print('\na1:\n',a1,'\na2:\n',a2,'\na3:\n',a3)

## forward transforms
Q10 = forwardQ_TRPY(-10,40,15,45,-30,0)

Q31 = np.array([[0.7071,0.7071,0,-10],
               [0,0,1,20],
               [0.7071,-0.7071,0,-5],
               [0,0,0,1]])

Q21 = np.array([[0,-1,0,3],
               [0,0,-1,6],
               [1,0,0,9],
               [0,0,0,1]])

pA_r3 = np.array([[18],
                  [12],
                  [-10],
                  [1]])

pB_r1 = np.array([[-6],
                  [4],
                  [2],
                  [1]])

Q_gripbase = forwardQ_TRPY(40,20,150,90,0,90)
Q_graspbase = forwardQ_TRPY(-70,20,200,90,0,115)

# print(np.linalg.inv(Q21) @ Q31)

# print(np.linalg.inv(Q21) @ Q31 @ pA_r3)
# print(np.linalg.inv(Q_gripbase) @ Q_graspbase)

forwardQ_TRPY(40,20,150,90,0,90)