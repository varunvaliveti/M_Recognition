import cv2 as cv



capture = cv.VideoCapture(0)

if not capture:
    exit()

while True:
    ret, frame = capture.read()

    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('f'):
        break

capture.release()
capture.destroyAllWindows()

