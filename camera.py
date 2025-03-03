import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector
# pylint: disable=no-member

detector = HandDetector(detectionCon=0.8, maxHands=2)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]['lmList']
        fingerUp = detector.fingersUp(hands[0])

        print(fingerUp)
        cnt.led(fingerUp)
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'No Dedos:0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'No Dedos:1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'No Dedos:2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'No Dedos:3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'No Dedos:4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'No Dedos:5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA) 
        elif fingerUp == [0, 1, 0, 0, 1]:
            cv2.putText(frame, 'No Dedos:2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 0, 0, 0]:
            cv2.putText(frame, 'No Dedos:2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)


    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()