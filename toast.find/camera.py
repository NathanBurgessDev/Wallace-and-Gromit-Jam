import cv2
from toastFinder import find_toast
import time

# watch for toast, and return two frames of toast positions to calculate
def watch_for_toast():
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    result = []

    while True:
        ret, frame = cam.read()

        # Display the captured frame
        cv2.imshow('Camera', frame)
        
        toast = find_toast(frame)
        if toast is not None and len(toast) > 2:
            result.append(toast)

            results = [x for x in result if x[2] >= time.time() - 1]
        
            if len(results) >= 3:
                print("3 found")
                break
        
        # Press 'q' to exit the loop
        if cv2.waitKey(10) == ord('q'):
            break

    # Release the capture and writer objects
    cam.release()
    cv2.destroyAllWindows()
    
def test_camera():
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

    while True:
        ret, frame = cam.read()

        # Write the frame to the output file
        out.write(frame)

        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cam.release()
    out.release()
    cv2.destroyAllWindows()