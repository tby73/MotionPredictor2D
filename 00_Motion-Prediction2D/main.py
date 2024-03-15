import cv2
import numpy as np

from detector import FaceDetector
from kalmanfilter import KalmanFilter

# cameras
DEFAULT_CAMERA = 0
SECONDARY_CAMERA = 1

# face detector path
FACE_DETECTOR_PATH = "Models/haarcascade_frontalface_default.xml"

# kalman filter params
CYCLE_DELAY = 0.1
ACCELERATION_X = ACCELERATION_Y = STD_ACC = 1
STD_MEAS_X = STD_MEAS_Y = 0.1

def main():
    video_cap = cv2.VideoCapture(DEFAULT_CAMERA)
    kf = KalmanFilter(CYCLE_DELAY, ACCELERATION_X, ACCELERATION_Y, STD_ACC, STD_MEAS_X, STD_MEAS_Y)

    while True:
        _, input_frame = video_cap.read()
        
        detector = FaceDetector(input_frame, detector_path=FACE_DETECTOR_PATH)
        face_cp = detector.DisplayFaces((0, 0), False)
        
        (x, y) = kf.Predict()
        (x1, y1) = kf.Update(face_cp)
        avg_vector_dir = ((x1 - x) / 2, (y1 - y) / 2)

        _ = detector.DisplayFaces(avg_vector_dir, True)

        cv2.imshow("MotionPredictor2D v1.0 - Visual Tracker", input_frame)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

    video_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

