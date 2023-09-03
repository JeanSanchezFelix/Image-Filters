import copy

def duplicate(image):
    new_image = []

    for row in image:
        tlst = []

        for col in row:
            tlst.append(col)
        new_image.append(tlst)

    return new_image


'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. That is to say each 
    pixel's grayscale value should be inverted relative to the maximum value of 255.
'''
def invert(image):
    nimage = duplicate(image)
    row =  len(image)
    column = len(image[0])

    for i in range(0,row):
        for j in range(0,column):

            nimage[i][j] = 255 - image[i][j] 
            
    return nimage



'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
'''
def flip(image):
    nimage = duplicate(image)
    nimage = image[::-1]

    return nimage



'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
'''
def blur(image):
    kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]

    nimage = duplicate(image)

    for y in range(len(image)):
        for x in range(len(image[y])):

            if y == 0 or x == 0 or y == len(image) - 1 or x == len(image[y]) - 1:
                nimage[y][x] = 0  

            else:
                total_weights = (
                        kernel[0][0] + kernel[0][1] + kernel[0][2] +
                        kernel[1][0] + kernel[1][1] + kernel[1][2] +
                        kernel[2][0] + kernel[2][1] + kernel[2][2] )

                weighted_sum = (
                    image[y-1][x-1] * kernel[0][0] + image[y-1][x] * kernel[0][1] + image[y-1][x+1] * kernel[0][2] +
                    image[y][x-1] * kernel[1][0] + image[y][x] * kernel[1][1] + image[y][x+1] * kernel[1][2] +
                    image[y+1][x-1] * kernel[2][0] + image[y+1][x] * kernel[2][1] + image[y+1][x+1] * kernel[2][2] )

                weighted_average = weighted_sum // total_weights
                nimage[y][x] = weighted_average
    return nimage



'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a 2x2 tiled version of the input image. The tile function
    will group pixels in groups of 4 and map each one to one of the 4 tiles
    based on their relative position in the group. That is to say in 
    [[1, 2],
     [3, 4]]
    the number 1 will be in the top left tile, 2 in the top right tile, 
    and so on. Because nearby pixels are similar this will create an image 
    which loops like 4 copies of the same image but slightly different.

    To make the transformation, consider 4 pixels in each iteration 
    of the loop and map them to the corresponding tiles. Each tile will be
    half the length and half the width of the input image.
'''
def tile(image):
    nimage = duplicate(image)
    row = len(image)
    column = len(image[0])

    half_y = row // 2
    half_x = column // 2

    for i in range(0, row, 2):
        for j in range(0, column, 2):
            nimage[i // 2][j // 2] = image[i][j] # New Tile 1       
            nimage[i // 2][j // 2 + half_x] = image[i][j+1] # New Tile 2
            nimage[i // 2 + half_y][j // 2] = image[i+1][j] # New Tile 3
            nimage[i // 2 + half_y][j // 2 + half_x] = image[i+1][j+1] # New Tile 4
    return nimage