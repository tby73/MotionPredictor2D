import cv2
import numpy as np

class KalmanFilter:
    def __init__(self, dt, acc_x, acc_y, std_acc, std_meas_x, std_meas_y) -> None:
        # sampling time
        self.dt = dt

        # acceleration in 2D
        self.acc = np.array([[acc_x], [acc_y]])
        
        # initial state
        self.x = np.array([[0], [0], [0], [0]])
        
        # State Transition Matrix
        self.A = np.array([[1, 0, self.dt, 0], 
                           [0, 1, 0, self.dt], 
                           [0, 0, 1, 0], 
                           [0, 0, 0, 1]])
        
        # Control Input Matrix
        self.B = np.array([[(self.dt ** 2) / 2, 0], 
                           [0, (self.dt ** 2) / 2], 
                           [self.dt, 0], 
                           [0, self.dt]])
        
        # Measurement Mapping Matrix
        self.H = np.array([[1, 0, 0, 0], 
                           [0, 1, 0, 0]])
        
        # Process Noise Covariance
        self.Q = np.array([[(self.dt ** 4) / 4, 0, (self.dt ** 3) / 2, 0], 
                           [0, (self.dt ** 4) / 4, 0, (self.dt ** 3) / 2], 
                           [(self.dt ** 3) / 2, 0, self.dt ** 2, 0], 
                           [0, (self.dt ** 3) / 2, 0, self.dt ** 2]]) + std_acc ** 2
        
        # Measurement Noise Covariance
        self.R = np.array([[std_meas_x ** 2, 0], [0, std_meas_y ** 2]])

        # Covariance Matrix
        self.P = np.eye(self.A.shape[1])

    def Predict(self):
        # update state 
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.acc)
        
        # calculate error covariance
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        
        return self.x[0:2]
    
    def Update(self, z):
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R

        # get kalman gain
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = np.round(self.x + np.dot(K, (z - np.dot(self.H, self.x))))
        I = np.eye(self.H.shape[1])

        # update error covariance
        self.P = (I - (K * self.H)) * self.P
        return self.x[0:2]
    
