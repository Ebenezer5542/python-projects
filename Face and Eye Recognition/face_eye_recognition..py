import cv2 as cv

def detect_faces_and_eyes():
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

    cap = cv.VideoCapture(0)

    # ↓ Set resolution lower for speed (e.g. 640x480)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Run detection every 5th frame
        if frame_count % 5 == 0:
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)
        frame_count += 1

        # Draw rectangles (optional)
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        for (a, b, c, d) in eyes:
            cv.rectangle(frame, (a, b), (a + c, b + d), (255, 0, 0), 1)

        cv.imshow("Fast Face & Eye Detection", frame)

        key = cv.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("s"):
            cv.imwrite("captured.jpg", frame)
            print("📸 Image saved!")

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    detect_faces_and_eyes()
