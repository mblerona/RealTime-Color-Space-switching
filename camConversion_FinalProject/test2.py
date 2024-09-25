import cv2
import numpy as np


def adjust_channels(frame, color_space, ch1, ch2, ch3):
    if color_space == 'RGB':
        frame[:, :, 0] = cv2.multiply(frame[:, :, 0], ch1 / 255)
        frame[:, :, 1] = cv2.multiply(frame[:, :, 1], ch2 / 255)
        frame[:, :, 2] = cv2.multiply(frame[:, :, 2], ch3 / 255)
    elif color_space == 'HSV':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame[:, :, 0] = cv2.multiply(frame[:, :, 0], ch1 / 255)
        frame[:, :, 1] = cv2.multiply(frame[:, :, 1], ch2 / 255)
        frame[:, :, 2] = cv2.multiply(frame[:, :, 2], ch3 / 255)
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    elif color_space == 'LAB':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        frame[:, :, 0] = cv2.multiply(frame[:, :, 0], ch1 / 255)
        frame[:, :, 1] = cv2.multiply(frame[:, :, 1], ch2 / 255)
        frame[:, :, 2] = cv2.multiply(frame[:, :, 2], ch3 / 255)
        frame = cv2.cvtColor(frame, cv2.COLOR_LAB2BGR)
    return frame


def create_trackbars(channel_values):
    # Destroy any existing trackbars
    cv2.destroyAllWindows()
    cv2.namedWindow('Color Space Visualization')

    # Create trackbars with the current channel values
    cv2.createTrackbar('Channel 1', 'Color Space Visualization', channel_values[0], 255, lambda x: None)
    cv2.createTrackbar('Channel 2', 'Color Space Visualization', channel_values[1], 255, lambda x: None)
    cv2.createTrackbar('Channel 3', 'Color Space Visualization', channel_values[2], 255, lambda x: None)


def main():
    cap = cv2.VideoCapture(0)
    color_space = 'RGB'

    # List to store channel values
    channel_values = [255, 255, 255]

    create_trackbars(channel_values)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Get trackbar positions
        ch1 = cv2.getTrackbarPos('Channel 1', 'Color Space Visualization')
        ch2 = cv2.getTrackbarPos('Channel 2', 'Color Space Visualization')
        ch3 = cv2.getTrackbarPos('Channel 3', 'Color Space Visualization')

        # Update channel values
        channel_values = [ch1, ch2, ch3]

        # Adjust channels based on the selected color space
        adjusted_frame = adjust_channels(frame.copy(), color_space, ch1, ch2, ch3)
        cv2.imshow('Color Space Visualization', adjusted_frame)

        # Key handling
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):  # Switch to RGB
            color_space = 'RGB'
            create_trackbars(channel_values)
        elif key == ord('h'):  # Switch to HSV
            color_space = 'HSV'
            create_trackbars(channel_values)
        elif key == ord('l'):  # Switch to LAB
            color_space = 'LAB'
            create_trackbars(channel_values)
        elif key == ord('c'):  # Capture frame
            cv2.imwrite('Images/captured_frame.png', adjusted_frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
