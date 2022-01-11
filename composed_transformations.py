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