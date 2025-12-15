
import numpy as np
from filterpy.kalman import KalmanFilter

def linear_assignment(cost_matrix):
    import scipy
    return scipy.optimize.linear_sum_assignment(cost_matrix)

class Track(object):
    def __init__(self, bbox):
        self.kf = KalmanFilter(dim_x=7, dim_z=4)
        self.kf.F = np.array([[1,0,0,0,1,0,0],
                              [0,1,0,0,0,1,0],
                              [0,0,1,0,0,0,1],
                              [0,0,0,1,0,0,0],
                              [0,0,0,0,1,0,0],
                              [0,0,0,0,0,1,0],
                              [0,0,0,0,0,0,1]])
        
        self.kf.H = np.array([[1,0,0,0,0,0,0],
                              [0,1,0,0,0,0,0],
                              [0,0,1,0,0,0,0],
                              [0,0,0,1,0,0,0]])

        self.kf.R *= 10
        self.kf.P *= 10
        self.kf.Q *= 0.01

        self.kf.x[:4] = bbox.reshape((4,1))
        self.time_since_update = 0
        self.id = Track.count
        Track.count += 1

    count = 0

    def update(self, bbox):
        self.time_since_update = 0
        self.kf.update(bbox)

    def predict(self):
        self.kf.predict()
        self.time_since_update += 1
        return self.kf.x[:4]

class Sort(object):
    def __init__(self):
        self.tracks = []

    def update(self, dets=np.empty((0,5))):
        new_tracks = []
        for track in self.tracks:
            pred = track.predict()
            new_tracks.append(track)

        self.tracks = new_tracks

        tracked_objects = []
        for det in dets:
            x1, y1, x2, y2, conf = det
            found = False
            for track in self.tracks:
                track.update(np.array([x1,y1,x2,y2]))
                tracked_objects.append([x1,y1,x2,y2,track.id])
                found = True
                break
            if not found:
                new_track = Track(np.array([x1,y1,x2,y2]))
                self.tracks.append(new_track)
                tracked_objects.append([x1,y1,x2,y2,new_track.id])
        return np.array(tracked_objects)
