import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector


cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon = 0.5, maxHands=2)


while(True):
    ret, frame = cap.read()
    hand, frame = detector.findHands(frame)
    if hand:
        hand1 = hand[0]
        lmList1 = hand1["lmList"]

        length, info, frame = detector.findDistance(lmList1[4][:2], lmList1[8][:2], frame)
    

    cv.imshow("Frame", frame)
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()    