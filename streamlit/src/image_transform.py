from PIL import Image, ImageOps

def image_transform(img, img_path):
    """
    Convert the image type and make sure it dispalys upright

    Args:
        img - jpg image
    Returns:
        img - pillow image
    """
    image = Image.open(img_path + img)
    image = ImageOps.exif_transpose(image)
    return image