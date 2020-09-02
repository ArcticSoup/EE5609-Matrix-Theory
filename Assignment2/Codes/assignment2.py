import numpy as np
import matplotlib.pyplot as plt

def angle_lines(a,b):
    '''Function to find the angle between two lines given their direction vectors a and b'''
    ab_dot = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    cos_theta = ab_dot/(norm_a*norm_b)
    theta = np.arccos(cos_theta)
    theta = np.degrees(theta)
    return theta

#Solution verification cases, p = 70/11, putting this value in the direction vectors
a = np.array([-3,20/11,2])
b = np.array([-30/11,1,-5])
print("Angle between the two line in degrees is:")
print(angle_lines(a,b))

