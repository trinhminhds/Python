import cv2
import dlib

# Read the image
img = cv2.imread(r"D:\\Learning_Project_Python\\Project_Face\\Test2.jpg")

# conver img 3D -> 2D
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# dlib: Load Face Recognition Detector
detector = dlib.get_frontal_face_detector()

# load the predictor
predictor = dlib.shape_predictor(
    r"D:\\Learning_Project_Python\\Project_Face\\shape_predictor_68_face_landmarks.dat"
)

# use detector to find face landmarks
faces = detector(gray)

for face in faces:
    x1 = face.left()  # left Point
    y1 = face.top()  # top Point
    x2 = face.right()  # right Point
    y2 = face.bottom()  # bottom Point

    # Draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)

    face_features = predictor(image=gray, box=face)

    # Loop through all 68 points
    for n in range(0, 68):
        x = face_features.part(n).x
        y = face_features.part(n).y

        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=2, color=(0, 0, 255), thickness=1)

# Show the image
cv2.imshow(winname="Face Recognition App", mat=img)

# Wait for a key press to exit
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()
