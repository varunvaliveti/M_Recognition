import cv2 as cv
from mtcnn.mtcnn import MTCNN
import os 

print("hi")
detector = MTCNN()

#given video (later will be changed to live stream) get the faces

imagePathArr = []
def extractFaces(videoPath, output, interval=5, padding=40):

    if not os.path.exists(output):
        os.makedirs(output)
    
    capture = cv.VideoCapture(videoPath)
    frameCount = 0
    faces = 0
    
    while True:

        ret, frame = capture.read()
        
        if not ret:
            break
        
        if frameCount % interval == 0:
            results = detector.detect_faces(frame)
        
            for result in results:
                x,y,w,h = result["box"]
                keypoints = result["keypoints"]

                x1 = max(0,x-padding)
                y1 = max(0,y-padding)
                x2 = min(frame.shape[1], x+w+padding)
                y2 = min(frame.shape[0],y+h+padding)
                face = frame[y1:y2, x1:x2]

                faceFileName = os.path.join(output, f"face_{faces}.jpg")
                cv.imwrite(faceFileName, face)
                faces+=1
        
        frameCount+=1

    capture.release()

    
videoPath = "test.mp4"
outputPath = "/Users/varunvaliveti/Desktop/CS Files/Personal /M_Recognition/green"
extractFaces(videoPath, outputPath, interval=5)
print("done")
