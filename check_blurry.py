import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread("blurry.png", cv2.IMREAD_GRAYSCALE)

# Check if image was loaded successfully
if img is None:
    raise FileNotFoundError("Image file 'page.png' not found or couldn't be read.")

# Compute the Laplacian variance (focus metric)
focus_metric = cv2.Laplacian(img, cv2.CV_64F).var()

# Define a threshold for blurriness (adjust this experimentally)
threshold = 15000

# Print the focus metric
print(f"Focus metric (variance of Laplacian): {focus_metric:.2f}")

# Assess if image is blurry
if focus_metric < threshold:
    print("Page is blurry")
else:
    print("Page is clear")
