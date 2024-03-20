import cv2

def record_video(output_file, duration_sec=30, capture_device=0):
    # Open the video capture device (camera)
    cap = cv2.VideoCapture(capture_device)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30  # Frames per second
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
    
    # Record video for the specified duration
    start_time = cv2.getTickCount() / cv2.getTickFrequency()  # Current time in seconds
    while (cv2.getTickCount() / cv2.getTickFrequency() - start_time) < duration_sec:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            print("Error: Failed to capture frame.")
            break
        out.write(frame)  # Write the frame to the output video
    
    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage
output_file = 'recorded_video.avi'  # Output video file name
duration_sec = 30  # Duration of the recorded video in seconds
capture_device = 0  # Camera device index (0 by default, change if necessary)

record_video(output_file, duration_sec, capture_device)

