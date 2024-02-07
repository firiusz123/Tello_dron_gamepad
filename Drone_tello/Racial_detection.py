from djitellopy import tello
import cv2
import mediapipe as mp

me = tello.Tello()
me.connect()

me.streamon()
mp_faces = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
faces_detector = mp_faces.FaceDetection(min_detection_confidence=0.2)


while True:
    img = me.get_frame_read().frame
    rgb_frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faces_detector.process(rgb_frame)
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw , _ = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
    cv2.imshow('Ractial Detection', img)
    cv2.waitKey(1)
