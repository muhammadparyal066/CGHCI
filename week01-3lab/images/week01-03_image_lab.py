#Name: Muhammad Paryal
#Roll Number: 2k24/CSME/37
from PIL import Image
import os

# Path setup
INPUT_PATH = "images/original.jpg"
OUTPUT_DIR = "images"

print("Lab 01-03: Image Processing Lab")

# Check if image exists
if not os.path.exists(INPUT_PATH):
    print(f"Error: {INPUT_PATH} nahi mila!")
    exit()

img = Image.open(INPUT_PATH)
print(f"Original Size: {img.size}, Mode: {img.mode}")

# 1. Grayscale
gray = img.convert("L")
gray.save(f"{OUTPUT_DIR}/grayscale.jpg")
print("Saved: grayscale.jpg")

# 2. Resize 50%
w, h = img.size
resized = img.resize((w//2, h//2))
resized.save(f"{OUTPUT_DIR}/resized.jpg")
print("Saved: resized.jpg")

# 3. Rotated 90 degree
rotated = img.rotate(90, expand=True)
rotated.save(f"{OUTPUT_DIR}/rotated_90.jpg")
print("Saved: rotated_90.jpg")

# 4. Flipped Horizontal
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped.save(f"{OUTPUT_DIR}/flipped.jpg")
print("Saved: flipped.jpg")

# 5. Thumbnail
thumb = img.copy()
thumb.thumbnail((100, 100))
thumb.save(f"{OUTPUT_DIR}/thumbnail.jpg")
print("Saved: thumbnail.jpg")

print("All tasks completed!")