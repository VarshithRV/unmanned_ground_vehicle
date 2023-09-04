import numpy as np

def rotate_inertia(I, theta):
    # Define the rotation matrix
    R = np.array([[np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    
    # Calculate the new inertia matrix
    I_prime = R @ I @ R.T
    
    return I_prime

I = np.array([[0.001421875, 0.0, 0],[0,0.001421875,0],[0,0,0.00234375]])
theta = np.pi/2
print(rotate_inertia(I, theta))