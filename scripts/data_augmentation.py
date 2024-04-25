#####
###
# 00 Imports
###
#####
import os
from PIL import Image




#####
###
# 01 Create rotated images
###
#####
def create_rotated_images(path, path_save):
    """
    Create rotated images.
    
    Args:
        path: path to the folder with images
        path_save: path to the folder where the new images will be saved
    
    Returns:
        None
    """

    # List all files in the folder
    files = os.listdir(path)

    # Loop through all files
    for file in files:
        # Open the image
        image = Image.open(path + file)
        
        # Rotate the image 0, 90, 180, 270 degrees
        image_0 = image.rotate(0)
        image_90 = image.rotate(90)
        image_180 = image.rotate(180)
        image_270 = image.rotate(270)
        
        # Save the new images
        image_0.save(path_save + file[:-4] + '_0.png')
        image_90.save(path_save + file[:-4] + '_90.png')
        image_180.save(path_save + file[:-4] + '_180.png')
        image_270.save(path_save + file[:-4] + '_270.png')

    # Print the number of images
    print('Number of images:', len(files))

    # Print the number of new images
    print('Number of new images:', len(os.listdir(path_save)))




#####
###
# 02 Create bright and dark contrast images
###
#####
def create_contrast_images(path, path_save):
    """
    Create bright and dark contrast images.
    
    Args:
        path: path to the folder with images
        path_save: path to the folder where the new images will be saved
    
    Returns:
        None
    """

    # List all files in the folder
    files = os.listdir(path)

    # Loop through all files
    for file in files:
        # Open the image
        image = Image.open(path + file)
        
        # Make the image 50% brighter
        image_bright = image.point(lambda p: p * 1.5)
        
        # Make the image 50% darker
        image_dark = image.point(lambda p: p * 0.5)
        
        # Save the new images
        image_bright.save(path_save + file[:-4] + '_bright.png')
        image_dark.save(path_save + file[:-4] + '_dark.png')

    # Print the number of images
    print('Number of images:', len(files))

    # Print the number of new images
    print('Number of new images:', len(os.listdir(path_save)))