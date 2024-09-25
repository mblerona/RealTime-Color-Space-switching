import cv2
import numpy as np


def adjust_channels(frame, color_space, ch1, ch2, ch3):
    if color_space == 'RGB':
        frame[:, :, 0] = cv2.multiply(frame[:, :, 0], ch1 / 255)
        frame[:, :, 1] = cv2.multiply(frame[:, :, 1], ch2 / 255)
        frame[:, :, 2] = cv2.multiply(frame[:, :, 2], ch3 / 255)
    elif color_space == 'HSV':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame[:, :, 0] = cv2.multiply(frame[:, :, 0], ch1 / 179)
        frame[:, :, 1] = cv2.multiply(frame[:, :, 1], ch2 / 255)
        frame[:, :, 2] = cv2.multiply(frame[:, :, 2], ch3 / 255)
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    elif color_space == 'LAB':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        frame[:, :, 0] = cv2.multiply(frame[:, :, 0], ch1 / 100)
        frame[:, :, 1] = cv2.multiply(frame[:, :, 1], ch2 / 255)
        frame[:, :, 2] = cv2.multiply(frame[:, :, 2], ch3 / 255)
        frame = cv2.cvtColor(frame, cv2.COLOR_LAB2BGR)
    return frame


def create_trackbars(color_space):
    if color_space == 'RGB':
        cv2.createTrackbar('R', 'Color Space Visualization', 255, 255, lambda x: None)
        cv2.createTrackbar('G', 'Color Space Visualization', 255, 255, lambda x: None)
        cv2.createTrackbar('B', 'Color Space Visualization', 255, 255, lambda x: None)
    elif color_space == 'HSV':
        cv2.createTrackbar('H', 'Color Space Visualization', 179, 179, lambda x: None)
        cv2.createTrackbar('S', 'Color Space Visualization', 255, 255, lambda x: None)
        cv2.createTrackbar('V', 'Color Space Visualization', 255, 255, lambda x: None)
    elif color_space == 'LAB':
        cv2.createTrackbar('L', 'Color Space Visualization', 100, 100, lambda x: None)
        cv2.createTrackbar('A', 'Color Space Visualization', 128, 255, lambda x: None)
        cv2.createTrackbar('B', 'Color Space Visualization', 128, 255, lambda x: None)


def main():

    cap = cv2.VideoCapture(0)
    color_space = 'RGB'
    cv2.namedWindow('Color Space Visualization')
    create_trackbars(color_space)

    while True:
        ret, frame = cap.read()
        if not ret:
            break


        ch1 = cv2.getTrackbarPos('R' if color_space == 'RGB' else 'H' if color_space == 'HSV' else 'L', 'Color Space Visualization')
        ch2 = cv2.getTrackbarPos('G' if color_space == 'RGB' else 'S' if color_space == 'HSV' else 'A', 'Color Space Visualization')
        ch3 = cv2.getTrackbarPos('B' if color_space == 'RGB' else 'V' if color_space == 'HSV' else 'B', 'Color Space Visualization')


        adjusted_frame = adjust_channels(frame.copy(), color_space, ch1, ch2, ch3)


        cv2.imshow('Color Space Visualization', adjusted_frame)


        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):  # Switch to RGB
            color_space = 'RGB'
            cv2.destroyAllWindows()
            cv2.namedWindow('RGB CS')
            create_trackbars(color_space)
        elif key == ord('h'):  # Switch to HSV
            color_space = 'HSV'
            cv2.destroyAllWindows()
            cv2.namedWindow('HSV CS')
            create_trackbars(color_space)
        elif key == ord('l'):  # Switch to LAB
            color_space = 'LAB'
            cv2.destroyAllWindows()
            cv2.namedWindow('LAB CS')
            create_trackbars(color_space)
        elif key == ord('c'):  # Capture frame
            cv2.imwrite('Images/captured_frame.png', adjusted_frame)


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
