import cv2

from visualization_utils import Display

class FaceDetector:
    def __init__(self, input_image, detector_path) -> None:
        self.input_image = input_image
        self.network_input = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
        self.detector = cv2.CascadeClassifier(detector_path)

    def GetFaces(self):
        return self.detector.detectMultiScale(self.network_input, 1.1, 5)
    
    def DisplayFaces(self, motion_vec_dir, draw=True):
        if draw:
            for x, y, w, h in self.GetFaces():
                center_point = Display.BoundingBoxwithDirectionVector(self.input_image, motion_vec_dir, x, y, w, h, (255, 255, 255), 2, True)
                return center_point
        else:
            for x, y, w, h in self.GetFaces():
                center_point = Display.BoundingBoxwithDirectionVector(self.input_image, motion_vec_dir, x, y, w, h, (255, 255, 255), 2, False)
                return center_point
