# Image-Filters


### Background:

Images are 2-dimensional arrays of individual color values for each pixel in the image. Each pixel is located using indices in a 2D array (list of lists) and takes on the color specified in the image file. Consider the following example:

```
cross = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
]
```
In this 2D list, 1 represents white, and 0 represents black. This specific 2D list creates an image of a white cross on a black background. 


For instance, assuming `cross` is a 2D list, the first index accesses an inner list item:

```
cross[0] == [0, 1, 0]
cross[1] == [1, 1, 1]
cross[2] == [0, 1, 0]
```

Then, the second index assumes you've already obtained the item from `cross` at the correct position and retrieves an item from the inner list:

```
cross[0][0] == [0,1,0][0] == 0
cross[1][0] == [1,1,1][0] == 1
cross[2][0] == [0,1,0][0] == 0
```

In this coordinate system, a pixel (y, x) is at row `y` and column `x`, where (0, 0) represents the top-left corner of the image. Larger `y` values correspond to positions farther down in the image.

### Working with Images:

Here is an example of how to visualize and open an image using Python libraries:

```python
%matplotlib inline
import sys
from skimage import io
import matplotlib.pyplot as plt
from random import choice

logo = io.imread('images/plussign.pbm')  # Reads the image as an array of integers
logo = logo.tolist()  # Converts it to a Python list
```
Grayscale often uses 8-bit resolution which means that 0 is pure black, 255 is pure white, and everything in between is shades of gray where the higher the number the brighter/lighter it is and the lower the number the darker it is.

## Filters:

### I. Invert Filter

The `invert` function takes a grayscale image as input, represented as a 2D list of integers. Its purpose is to create and return a new image that is an inverted version of the input image. In this context, an inverted image means switching the values of black and white, where black pixels become white, and white pixels become black.

### II. Flip Filter

The `flip` function is designed to flip a given image vertically. In other words, it takes an input image represented as a 2D list of pixels and returns a new image where the rows of pixels have been reversed. This operation effectively flips the image vertically, making the first row swap with the last row, the second row swap with the second-to-last row, and so on.

### III. Blur Filter 

The `blur` function is designed to apply a blur filter to an input image, which is represented as a 2D list of pixel values. This blur filter is commonly used to smooth out noisy images or images with low quality. The idea behind the blur filter is to average the pixel values of a pixel with those of its neighboring pixels. This process helps to reduce variations and noise in the image.


1. **Pixel Neighbors**: For each pixel at position (y, x) in the image, the function considers its neighbors. A pixel's neighbors include all adjacent pixels, including diagonals, as shown below:

   ```
   image[y-1][x-1] | image[y-1][ x ] | image[y-1][x+1]
   ---------------------------------------------------
   image[ y ][x-1] | image[ y ][ x ] | image[ y ][x+1]
   ---------------------------------------------------
   image[y+1][x-1] | image[y+1][ x ] | image[y+1][x+1]
   ```

   
2. **Kernel**: There is a 2D list called `kernel`, which holds the weights of each pixel value when applying the blur filter. This kernel is essential as it ensures that each pixel's value is given higher importance than that of its neighbors. This emphasis on the central pixel helps preserve important image features, such as boundaries between objects, while smoothing out variations in pixel values.
   

3. **Edge Handling**: The function identifies edge pixels, which are pixels that don't have all neighbors. An edge pixel is defined as a pixel at position (Y, X) where at least one of the following conditions is true:
   - Y == 0
   - Y == len(image) - 1
   - X == 0
   - X == len(image[y]) - 1

   For edge pixels, the function sets their value to 0, as the weighted average formula doesn't apply to them.

### IV. Tile Filter

The `tile` filter function takes an input image represented as a 2D list and creates a 2x2 tiled version of the original image. In this tiled version, there are four copies of the original image. Each tile is half the width and half the height of the original image. 


1. **Quadrant Mapping**: To create the tiled effect, the function processes the image in groups of 4 pixels. For each group, it maps each pixel to one of the 4 quadrants based on its relative position within the group. Specifically:

   ```
   |  pixel( i, j)  |  pixel( i, j+1)  | 
   -------------------------------------
   | pixel( i+1, j) | pixel( i+1, j+1) | 
   ```
3. **Tile Size Calculation**: The function calculates the dimensions of the new image, which will be half the width and half the height of the original image. These dimensions are stored in `half_y` and `half_x`.

4. **Pixel Mapping**: The function uses nested loops to iterate through the rows and columns of the original image, grouping pixels in 2x2 sections. For each section, it maps the pixels to the corresponding locations in the new image according to the rules described above.
