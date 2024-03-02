from flask import Flask, render_template
import cv2
from gaze_tracking import GazeTracking

app = Flask(__name__, template_folder='keerthan')

# Initialize gaze tracking and webcam
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

@app.route('/')
def index():
    # Analyze the frame using gaze tracking
    _, frame = webcam.read()
    gaze.refresh(frame)
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    # Pass the gaze tracking information to the template
    return render_template('index.html', gaze_text=text)

if __name__ == '__main__':
    app.run(debug=True)

# Release the webcam resources
webcam.release()
cv2.destroyAllWindows()

