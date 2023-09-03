from PIL import Image
import numpy as np
import sys
import os
import filecmp

# The following CONSTANTS point to the folders/directories with images 
# and the names of the functions in the student code file to test
# CHANGE AT YOUR OWN RISK
RESULT_DIR = 'resulting_images'
IMAGE_DIR = 'images'
EXPECTED_DIR = 'expected_images'

np.set_printoptions(threshold=np.inf)

def image_file_to_2D_list(filename, mode='L'):
    filename = os.path.abspath(filename)
    with Image.open(filename) as fd:
        return np.asarray(fd.convert(mode))

def arr_to_im(array, mode='L'):
    return Image.fromarray(np.uint8(array), mode=mode)

def save_as_image_file(array, filename, mode='L'):
    arr_to_im(array, mode).save(filename)

def run_student_code(filename):
    with open(filename, 'r') as fd:
        code = compile(fd.read(), filename, 'exec')
    return code

def test_code(imageName, functions):
    im = image_file_to_2D_list(imageName)
    out = []
    for f in functions:
        newim = arr_to_im(f(im))
        out.append( (newim, f.__name__) )
    return out

if __name__ == '__main__':
    args = sys.argv[1:]
    if not len(args) or not args[0].endswith('.py'):
        print('Must provide path to student code (\'.py\' file)!!!')
        sys.exit(-1)
    # Here we know args has path to a .py file
    try:
        exec(run_student_code(args[0]))
    except:
        print('Could not run the given file:', args[0])
        sys.exit(-2)
    # Here we already have the student functions running on this file
    # make a directory for the resulting images if needed
    if not os.path.isdir(RESULT_DIR):
        os.mkdir(RESULT_DIR)
    # for all images in the image directory
    for image in os.listdir(IMAGE_DIR):
        name = os.path.join(IMAGE_DIR, image)  # get the full path from current directory
        try:
            # Remove ') #' if you implemented the tile function and want to test it.
            FUNCTIONS = (blur, flip, invert) #, tile)
            modified = test_code(name, FUNCTIONS)  # runs the filters
        except NameError as err:  # catches errors due to nonexistant functions
            print(err)
            sys.exit(-3)

        names = []
        for newim, func in modified:
            dot = image.index('.')
            newname = image[:dot] + func + image[dot:]  # new name to save each image
            names.append(newname)  # store for use with expected images
            save_as_image_file(newim, os.path.join(RESULT_DIR, newname))  # saves image to result directory
        # checks if the images from student filter matches the expectation
        _, mismatch, errs = filecmp.cmpfiles(RESULT_DIR, EXPECTED_DIR, names)
        failed = mismatch + errs
        if failed:  # failed for some file, print error message
            [print(f'Function: {i} failed for {image}') for i in failed]
        else:  # nothing failed
            print(f'All filters passed for {image}')
        # uncomment next line to open the images when running the code.
        # [im[0].show() for im in modified]

