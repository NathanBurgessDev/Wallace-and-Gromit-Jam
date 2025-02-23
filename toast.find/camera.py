import cv2
from toastFinder import find_toast
from JamFiring import fireJam
import time, os, glob

# watch for toast, and return two frames of toast positions to calculate
def watch_for_toast():
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    result = []

    inputImages = []
    outputImages = []

    while True:
        ret, frame = cam.read()

        # Display the captured frame
        cv2.imshow('Camera', frame)
        
        toast = find_toast(frame)
        if toast is not None and len(toast) > 2:
            print("i see toast")
            fireJam()
            #TODO: figure out where to shoot
        #     outputImages = [x[3] for x in result if x[2] >= time.time() - 0.5]
        #     inputImages = [x[4] for x in result if x[2] >= time.time() - 0.5]
            
        #     result.append(toast)

        #     result = [x for x in result if x[2] >= time.time() - 0.5]
        
        #     if len(result) >= 3:
        #         print("3 found")
        #         break
        
        # Press 'q' to exit the loop
        if cv2.waitKey(20) == ord('q'):
            break

    for input in inputImages:
        cv2.imwrite(f"Input{len(result)}.png", input)

    for output in outputImages:
        cv2.imwrite(f"Output{len(result)}.png", output)

    # Release the capture and writer objects
    cam.release()
    cv2.destroyAllWindows()
    return result
    
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