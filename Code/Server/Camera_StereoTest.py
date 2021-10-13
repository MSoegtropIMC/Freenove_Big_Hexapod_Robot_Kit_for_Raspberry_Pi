import cv2
import time

camL = cv2.VideoCapture(0)
camR = cv2.VideoCapture(2)

if not camL.isOpened() or not camR.isOpened():
    print("Error opening camera")
    exit(1)

camL.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camL.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camL.set(cv2.CAP_PROP_FPS , 15)
camR.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camR.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camR.set(cv2.CAP_PROP_FPS , 15)

# grab a few frames to make auto exposure correct

print("start")

for _ in range(1,30):
    camL.grab()
    camR.grab()

print("end")

camL.grab()
camR.grab()

retL, frameL = camL.retrieve()
retR, frameR = camR.retrieve()

if retL:
    cv2.imwrite("Test1L.jpg",frameL)
if retR:
    cv2.imwrite("Test1R.jpg",frameR)

print("OK")
