import numpy as np
import cv2
import os

class ImageGenerator:
    def __init__(self, width=300, height=300):
        self.width = width
        self.height = height
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)  # Black background by default
    
    def background(self, color):
        self.image[:, :] = color
    
    def circle(self, center, radius, color):
        cv2.circle(self.image, center, radius, color, -1)

    def save_image(self, filename):
        folder = "gray_hues"
        if not os.path.exists(folder):
            os.makedirs(folder)
        cv2.imwrite(os.path.join(folder, filename), self.image)

# Initialize the image generator
generator = ImageGenerator()

# Define the background color
background_color = (255, 255, 255)  # Green background

# # Generate 10 images with slightly different circle colors
for i in range(10):
    # Adjust the green hue for each iteration
    hue = (i) % 180  # Increment the hue by 5 for each iteration (180 is the maximum value for hue in OpenCV)
    circle_color = (245-hue, 245-hue, 245-hue)  # Varying hue in BGR color space

    # Set the background color and draw the circle
    generator.background(background_color)
    generator.circle((150, 150), 100, circle_color)

    # Save the image with a filename indicating the hue
    filename = f"image_{245-hue}.jpg"
    generator.save_image(filename)

# Set the background color and draw the circle
# generator.background(background_color)
# generator.circle((150, 150), 100, (0,250,0))

# # Save the image with a filename indicating the hue
# filename = f"image_0_hue_250.jpg"
# generator.save_image(filename)
