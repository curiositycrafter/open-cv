import cv2
import time

cap = cv2.VideoCapture(0)

# Get frame properties
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)          # 1️⃣ STORE frame
    cv2.imshow("Live", frame) # 2️⃣ DISPLAY frame

    if time.time() - start_time >= 10:  # 3️⃣ STOP after 10 sec
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()