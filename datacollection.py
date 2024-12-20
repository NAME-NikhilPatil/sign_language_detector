# import cv2
# from cvzone.HandTrackingModule import HandDetector
# import numpy as np
# import math
# import time
#
# cap = cv2.VideoCapture(0)
# detector = HandDetector(maxHands=1)
# offset = 20
# imgSize = 300
# counter = 0
#
# folder = "Data/Okay"
#
# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)
#     if hands:
#         hand = hands[0]
#         x, y, w, h = hand['bbox']
#
#         imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
#
#         imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
#         imgCropShape = imgCrop.shape
#
#         aspectRatio = h / w
#
#         if aspectRatio > 1:
#             k = imgSize / h
#             wCal = math.ceil(k * w)
#             imgResize = cv2.resize(imgCrop, (wCal, imgSize))
#             imgResizeShape = imgResize.shape
#             wGap = math.ceil((imgSize-wCal)/2)
#             imgWhite[:, wGap: wCal + wGap] = imgResize
#
#         else:
#             k = imgSize / w
#             hCal = math.ceil(k * h)
#             imgResize = cv2.resize(imgCrop, (imgSize, hCal))
#             imgResizeShape = imgResize.shape
#             hGap = math.ceil((imgSize - hCal) / 2)
#             imgWhite[hGap: hCal + hGap, :] = imgResize
#
#         cv2.imshow('ImageCrop', imgCrop)
#         cv2.imshow('ImageWhite', imgWhite)
#
#     cv2.imshow('Image', img)
#     key = cv2.waitKey(1)
#     if key == ord("s"):
#         counter += 1
#         cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
#         print(counter)

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os

# Create folder if it doesn't exist
if not os.path.exists("Data/Hello"):
    os.makedirs("Data/Hello")

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300
counter = 0

folder = "Data/Hello"

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        try:
            imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap: wCal + wGap] = imgResize

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap: hCal + hGap, :] = imgResize

            cv2.imshow('ImageCrop', imgCrop)
            cv2.imshow('ImageWhite', imgWhite)

        except Exception as e:
            print(f"Error during cropping or resizing: {e}")
    else:
        imgWhite = None  # Ensure imgWhite is reset when no hand is detected

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord("s") and imgWhite is not None:
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(f"Saved Image {counter}")
    elif key == ord('q'):  # Exit the loop on 'q'
        break

cap.release()
cv2.destroyAllWindows()
