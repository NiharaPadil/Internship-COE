import pandas as pd
from PIL import Image
import numpy as np

# Load the image
image_path = 'C:/Users/sanks/Sahyadri/Internships/Internship-II/Tasks/Flag_of_Japan.svg.png"'  # Replace with the path to your image file
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Create a DataFrame from the NumPy array
df = pd.DataFrame(image_array)

# Specify the Excel file name and sheet name
excel_file = 'Image_Matrix.xlsx'
sheet_name = 'ImageSheet'

# Write the DataFrame to an Excel file
df.to_excel(excel_file, sheet_name=sheet_name, index=False)

print(f"Image data saved to '{excel_file}' in sheet '{sheet_name}'")
