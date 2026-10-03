# Computer Graphics Lab - Assignment

## Overview
This assignment covers basic image processing techniques using Python and NumPy. We solved 5 core problems related to image enhancement and edge detection.

## Tools Used
- Python 3.13
- NumPy library
- Visual Studio Code

## How We Solved The Tasks

### Problem 1 & 2: Thresholding and Brightness Adjustment
We used simple if-else condition for thresholding and basic arithmetic for brightness. To prevent pixel values from going out of range (0-255), we used `np.clip()` and converted the data type back to `uint8` using `astype()`.

**Key Learning:** How pixel intensity works and how to control over-brightness.

### Problem 3: Mean Filter (Blurring)
We implemented a 3x3 mean filter. The logic was to add all 9 pixels of the neighborhood and divide by 9. We used `np.mean()` and `round()` to get the average value. This helps in reducing noise in an image.

Formula: `mean = sum(all 9 pixels) / 9`

### Problem 4: Contrast Stretching
We stretched the contrast of a dark image to a full dynamic range (0-255). We used the standard formula:
`stretched = (image - in_min) / (in_max - in_min) * (out_max - out_min) + out_min`
And used `np.clip()` to keep values in range.

### Problem 5: Sobel Edge Detection
This was the most advanced task. We created two 3x3 kernels:
- Gx for horizontal edges
- Gy for vertical edges

We multiplied the image block with these kernels, summed them to get `gx` and `gy`, and then calculated edge strength using `sqrt(gx^2 + gy^2)`.

**Key Learning:** How edge detection algorithms find boundaries in an image.

## Results
All 5 problems passed successfully in the terminal:
- Problem 1 passed
- Problem 2 passed
- Problem 3 passed
- Problem 4 passed
- Problem 5 passed

## Author
Muhammad Paryal - BS Computer Science
Roll Number - 2k24/CSME/37