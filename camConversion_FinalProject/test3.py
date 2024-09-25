import cv2
import numpy as np
from tkinter import Tk, Scale, Label, Button, HORIZONTAL, StringVar, IntVar

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


def update_color_space(color_space_var, channel_vars):
    # Function to switch color spaces and update the interface
    global color_space
    color_space = color_space_var.get()
    update_labels()


def capture_frame():
    global adjusted_frame
    cv2.imwrite('Images/captured_frame.png', adjusted_frame)


def update_labels():
    label_color_space.config(text=f"Color Space: {color_space}")
    label_ch1.config(text=f"Channel 1: {channel_vars[0].get()}")
    label_ch2.config(text=f"Channel 2: {channel_vars[1].get()}")
    label_ch3.config(text=f"Channel 3: {channel_vars[2].get()}")


def main():
    global adjusted_frame, color_space, label_color_space, label_ch1, label_ch2, label_ch3, channel_vars

    # Initialize tkinter window
    root = Tk()
    root.title("Color Space Visualization")

    # Initial settings
    color_space = 'RGB'
    channel_vars = [IntVar(value=255), IntVar(value=255), IntVar(value=255)]

    # Camera setup
    cap = cv2.VideoCapture(0)

    # Sliders for channel adjustment
    slider_ch1 = Scale(root, from_=0, to=255, orient=HORIZONTAL, variable=channel_vars[0], label="Channel 1")
    slider_ch1.pack()
    slider_ch2 = Scale(root, from_=0, to=255, orient=HORIZONTAL, variable=channel_vars[1], label="Channel 2")
    slider_ch2.pack()
    slider_ch3 = Scale(root, from_=0, to=255, orient=HORIZONTAL, variable=channel_vars[2], label="Channel 3")
    slider_ch3.pack()

    # Labels for showing the current color space and channel values
    label_color_space = Label(root, text=f"Color Space: {color_space}")
    label_color_space.pack()
    label_ch1 = Label(root, text=f"Channel 1: {channel_vars[0].get()}")
    label_ch1.pack()
    label_ch2 = Label(root, text=f"Channel 2: {channel_vars[1].get()}")
    label_ch2.pack()
    label_ch3 = Label(root, text=f"Channel 3: {channel_vars[2].get()}")
    label_ch3.pack()

    # Buttons to switch color spaces
    color_space_var = StringVar(value=color_space)
    button_rgb = Button(root, text="RGB", command=lambda: update_color_space(color_space_var, channel_vars))
    button_rgb.pack()
    button_hsv = Button(root, text="HSV", command=lambda: update_color_space(color_space_var, channel_vars))
    button_hsv.pack()
    button_lab = Button(root, text="LAB", command=lambda: update_color_space(color_space_var, channel_vars))
    button_lab.pack()

    # Button to capture frame
    button_capture = Button(root, text="Capture Frame", command=capture_frame)
    button_capture.pack()

    # Continuously update the frame
    def update_frame():
        global adjusted_frame

        ret, frame = cap.read()
        if not ret:
            return

        # Get channel values
        ch1 = channel_vars[0].get()
        ch2 = channel_vars[1].get()
        ch3 = channel_vars[2].get()

        # Adjust channels based on the selected color space
        adjusted_frame = adjust_channels(frame.copy(), color_space, ch1, ch2, ch3)
        cv2.imshow('Color Space Visualization', adjusted_frame)

        # Update labels to reflect current values
        update_labels()

        # Continue updating
        root.after(10, update_frame)

    # Start updating frames
    update_frame()

    # Start tkinter main loop
    root.mainloop()

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
