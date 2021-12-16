
#################################
##--- VictorDamian
##--- Python 3.7.8 - OpenCV 3.5.3
##--- INFO: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
#################################
import cv2 as cv
import sys
class FaceDetection:
    
    def __init__(self, roi):
        self.ROI = roi
        self.font = cv.FONT_HERSHEY_SIMPLEX
        self.font_color = (255, 255, 255) 
        self.color_box = (0,0,0)

    def labelText(self, box, text):
        (startX, startY, endX, endY) = box
        #Box
        cv.rectangle(self.ROI, (startX,startY), ((startX+endX), startY+endY), self.color_box, 2)
        #Box label
        cv.rectangle(self.ROI, (startX-1,startY),((startX+endX)+1,startY-19), self.color_box,-1) 
        #Text
        cv.putText(self.ROI, text, (startX,startY-3), self.font, .6, self.font_color, 1, cv.LINE_AA)
        print(f'Coordenadas: 'f'{str(box)}')

    def faceDetector(self, frame):
        label = FaceDetection(roi=frame)
        cascade = cv.CascadeClassifier('files/haarcascade_frontalface_default.xml')
        face = cascade.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=11,
                minSize=(50,50),
                maxSize=(400,400)
        )
        for i in face:
            label.labelText(box=i, text='Rostro')

    def openFile(image):
        img = cv.imread(cv.samples.findFile(image))
        if img is None:
            sys.exit('No se pudo leer la imagen')
        FaceDetection.faceDetector(self=None, frame=img)
        cv.imshow("Face Detection", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def resizeImg(image,window_height):
        #print('Normal size: ', image.shape)
        aspect_ratio = float(image.shape[1])/float(image.shape[0])
        window_width = window_height/aspect_ratio
        image = cv.resize(image, (int(window_height),int(window_width)))
        cv.imshow("Resized", image)
        #print('Resize: ', image.shape)
        return image

    def openVideoOrCam(video):
        cap = cv.VideoCapture(video if video else 0, cv.CAP_DSHOW)
        if not cap.isOpened():
            print('Error al capturar stream')
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print('Error de frame')
                break
            FaceDetection.faceDetector(frame=frame)
            FaceDetection.resizeImg(image=frame, window_height=800)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()

### Deteccion con imagenes
_pathImg = 'files/ellen3.jpg'
FaceDetection.openFile(image=_pathImg)

## Deteccion en stream
#Ip a stream de video, 0 o 1 web cam
_ip = 'rtsp://x.x.x.x:0000'
_pathVideo = 'files/videoEntrada.mp4'
#FaceDetection.openVideoOrCam(video=_pathVideo)