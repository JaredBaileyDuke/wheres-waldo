#####
###
# 00 Imports
###
#####

import os
from PIL import Image




#####
###
# 01 Read in images
###
#####

def read_images(images_listdir):
    """
    Read in images from a list of image names.
    
    Args:
        images_listdir: list of image names
    
    Returns:
        images_dict: dictionary with image names as keys and PIL image objects as values
    """
    images_dict = {}
    for image_name in images_listdir:
        if image_name.endswith(".JPG"):
            image = Image.open(train_path + image_name)
            images_dict[image_name] = image
            print("Image " + image_name + " has been read in.")
    return images_dict




#####
###
# 02 Break images into tiles
###
#####    

# Function to break the image into tiles
def tile_image(image, tile_size=640, overlap=40):
    """
    Break an image into tiles.
    
    Args:
        image: PIL image object
        tile_size: size of the tiles
        overlap: overlap between tiles
        
    Returns:
        tiles: list of PIL image objects
    """

    # reset metadata of image rotation to 0
    image = image.rotate(270, expand=True)

    # Get the image size
    width, height = image.size
    
    # Create a list to store the tiles
    tiles = []
    
    # Loop through the image and break it into tiles
    for x in range(0, width, tile_size - overlap):
        for y in range(0, height, tile_size - overlap):
            # Get the tile
            tile = image.crop((x, y, x + tile_size, y + tile_size))
            tiles.append(tile)
    
    return tiles

# Function to save the tiles
def save_tiles(tiles, image_name, save_path):
    """
    Save the tiles as individual images.

    Args:
        tiles: list of PIL image objects
        image_name: name of the original image
        save_path: path to save the tiles
    """

    for i, tile in enumerate(tiles):
        if len(str(i)) == 1:
            tile.save(save_path + image_name + "_0" + str(i) + ".jpg")
        else:
            tile.save(save_path + image_name + "_" + str(i) + ".jpg")

# Loop through the images and break them into tiles
def break_images_into_tiles(images_dict, tile_size, overlap, tile_path):
    """
    Break images into tiles and save them.

    Args:
        images_dict: dictionary with image names as keys and PIL image objects as values
        tile_size: size of the tiles
        overlap: overlap between tiles
        tile_path: path to save the tiles

    Returns:
        None
    """

    for image_name, image in images_dict.items():
        tiles = tile_image(image, tile_size, overlap)
        save_tiles(tiles, image_name, tile_path)
        print("Image " + image_name + " has been broken into " + str(len(tiles)) + " tiles.")
