from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
import csv
import os
from PIL import Image


# Function to process a single image
def process_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    file_name = os.path.basename(image_path)
    return (file_name, width, height)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Pixel Size Generator by BioStemCore')
        self.setFixedSize(720, 480)

        # Create labels and entry box
        title_label = QLabel("Enter Image Folder Pathname:")
        self.pathname_entry = QLineEdit()  # Class member variable

        # Create output button
        output_button = QPushButton("Output")
        output_button.clicked.connect(lambda: self.mass_process_image())  # Pass self implicitly

        # Layout using QGridLayout
        layout = QGridLayout()
        layout.addWidget(title_label, 0, 0)
        layout.addWidget(self.pathname_entry, 0, 1)
        layout.addWidget(output_button, 1, 0, 1, 2)  # Span across 2 columns

        self.setLayout(layout)
        self.show()

    def mass_process_image(self):
        # Get pathname from class member variable
        pathname = self.pathname_entry.text()
        if not pathname:
            print("Folder path is empty.")
            return

        # List all .tif files in the folder
        image_paths = [os.path.join(pathname, f) for f in os.listdir(pathname) if f.endswith('.tif')]  # Filter for .tif files

        # Process all images and collect data
        data = []
        for image_path in image_paths:
            try:
                # Call process_image function for each image
                file_name, width, height = process_image(image_path)
                data.append((file_name, width, height))
            except Exception as e:  # Handle potential errors during image processing
                print(f"Error processing image {image_path}: {e}")

        # Write data to a CSV file (assuming data is a list of tuples)
        if data:
            with open('output.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['File Name', 'Width', 'Height'])  # Write header
                csv_writer.writerows(data)  # Write data
            print("Processing complete. Output saved to output.csv")


if __name__ == '__main__':
    app = QApplication([])
    window = App()
    app.exec_()
