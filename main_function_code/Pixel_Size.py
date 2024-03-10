from PIL import Image
import csv
import os

# Function to process a single image
def process_image(image_path):
    # Open the image
    img = Image.open(image_path)
    # Get image size
    width, height = img.size
    # Get file name
    file_name = os.path.basename(image_path)
    # Return the data as a tuple
    return (file_name, width, height)

# Specify the folder path
folder_path = '/Users/mertegemencaliskan/Downloads/ONH/PAR/1'

# List all .tiff files in the folder
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.tif')]

# Process all images and collect data
data = [process_image(path) for path in image_paths]

# Write data to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['File Name', 'Width', 'Height']) # Write header
    csv_writer.writerows(data) # Write data

print("Data written to output.csv")
