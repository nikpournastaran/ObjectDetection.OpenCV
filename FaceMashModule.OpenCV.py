import cv2 as cv
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv.VideoCapture(0)
detector = FaceDetector()
meshdetector = FaceMeshDetector(maxFaces=1)


while(True):
    ret, frame = cap.read()
    frame,bbox = detector.findFaces(frame)
    frame, faces = meshdetector.findFaceMesh(frame)



    if bbox:
        center = bbox[0]["center"]


    

    cv.imshow("Frame", frame)
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()    