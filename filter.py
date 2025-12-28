import cv2
import sys
import numpy as np

PREVIEW  = 0
BLUR     = 1
FEATURES = 2
CANNY    = 3

feature_params = dict(
    maxCorners=500,
    qualityLevel=0.2,
    minDistance=15,
    blockSize=9
)

# Camera source (0 = webcam)
cam_src = 0
if len(sys.argv) > 1:
    cam_src = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Use familiar name: cap
cap = cv2.VideoCapture(cam_src)

while alive:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Default output
    img_result = frame

    if image_filter == CANNY:
        img_result = cv2.Canny(frame, 80, 150)

    elif image_filter == BLUR:
        img_result = cv2.blur(frame, (13, 13))

    elif image_filter == FEATURES:
        img_result = frame.copy()
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        corners = cv2.goodFeaturesToTrack(img_gray, **feature_params)
        if corners is not None:
            for x, y in np.float32(corners).reshape(-1, 2):
                cv2.circle(img_result, (int(x), int(y)), 10, (0, 255, 0), 1)

    cv2.imshow(win_name, img_result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q') or key == 27:
        alive = False
    elif key == ord('c'):
        image_filter = CANNY
    elif key == ord('b'):
        image_filter = BLUR
    elif key == ord('f'):
        image_filter = FEATURES
    elif key == ord('p'):
        image_filter = PREVIEW

cap.release()
cv2.destroyAllWindows()
