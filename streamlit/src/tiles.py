from PIL import Image

def tile_image(image, tile_size, overlap):
    """
    A function to break an image into tiles
    Args:
        image: The image to break into tiles
        tile_size: The size of the tiles
        overlap: The overlap between tiles
    Returns:
        A list of tiles
    """
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