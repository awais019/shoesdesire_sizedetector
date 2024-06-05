import cv2
import numpy as np


def get_foot_size(image_path, paper_size=(297, 210)):  # A4 paper size in mm
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assuming largest contour is the foot
    foot_contour = max(contours, key=cv2.contourArea)

    # Get bounding box of the foot contour
    x, y, w, h = cv2.boundingRect(foot_contour)

    # Calculate real-world measurements
    # Assuming the longer side of the paper is aligned with the longer side of the image
    pixel_to_mm_ratio = paper_size[1] / \
        image.shape[1] if image.shape[0] > image.shape[1] else paper_size[0] / image.shape[1]
    foot_length = w * pixel_to_mm_ratio
    foot_width = h * pixel_to_mm_ratio

    return foot_length, foot_width
