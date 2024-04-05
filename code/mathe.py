import numpy as np

def rotate_polygon(points,angle,center):
    pi_angle = angle*np.pi
    R = [[np.cos(pi_angle), -np.sin(pi_angle)],
                [np.sin(pi_angle), np.cos(pi_angle)]]
    P = np.transpose(points)
    C =  [np.transpose(center) for point in points]
    C = np.transpose(C)
    sub = P-C
    res = np.transpose(np.matmul(R,sub) + C)
    return res

