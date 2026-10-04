#Name: Muhammad Paryal
#Roll Number: 2k24/CSME/37
from PIL import Image
import os

# Path setup - file is INSIDE images folder
INPUT_PATH = "original.jpg"
OUTPUT_DIR = "."

print("Lab 01-03: Image Processing Lab")

# Check if image exists
if not os.path.exists(INPUT_PATH):
    print(f"Error: {INPUT_PATH} nahi mila!")
    exit()

img = Image.open(INPUT_PATH)
print(f"Original Size: {img.size}, Mode: {img.mode}")

# 1. Grayscale
gray = img.convert("L")
gray.save(os.path.join(OUTPUT_DIR, "grayscale.jpg"))
print("Saved grayscale.jpg")

# 2. Resized
resized = img.resize((100, 100))
resized.save(os.path.join(OUTPUT_DIR, "resized.jpg"))
print("Saved resized.jpg")

# 3. Flipped
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped.save(os.path.join(OUTPUT_DIR, "flipped.jpg"))
print("Saved flipped.jpg")

# 4. Rotated
rotated = img.rotate(90, expand=True)
rotated.save(os.path.join(OUTPUT_DIR, "rotated_90.jpg"))
print("Saved rotated_90.jpg")

# 5. Thumbnail
thumb = img.copy()
thumb.thumbnail((50, 50))
thumb.save(os.path.join(OUTPUT_DIR, "thumbnail.jpg"))
print("Saved thumbnail.jpg")

print("All tasks completed!")