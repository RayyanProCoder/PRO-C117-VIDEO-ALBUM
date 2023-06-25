import os
import cv2

# Set path for the Images folder
path = "Project117/Images"

# Create a list variable named Images
images = []

# Check each file in the folder
for file in os.listdir(path):
    # Separate the name and extension from the file name
    name, extension = os.path.splitext(file)
    
    # Check if the extension matches the image extension
    if extension.lower() in ['.jpg', '.jpeg', '.png']:
        # Create the file name by concatenating the path and filename
        file_name = os.path.join(path, file)
        
        # Print the file name to check if filenames are formed correctly
        print(file_name)
        
        # Add the file to the images list
        images.append(file_name)

# Get the count of images
count = len(images)

# Read the first image from the images list
frame = cv2.imread(images[0])

# Capture width, height, and channels
width, height, channels = frame.shape

# Create a tuple variable size using width and height
size = (width, height)

# Print the size to check the result
print(size)

# Create a VideoWriter
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Add images to the video writer
for i in range(0, count):
    # Read each image
    image = cv2.imread(images[i])
    
    # Add the image to the video
    out.write(image)

# Release the video writer
out.release()

# Print a message to indicate the video is complete
print("Done")
