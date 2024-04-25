#####
###
# 00 Imports
###
#####

import os
from PIL import Image
from ultralytics import YOLO
from scripts.tiling import *
from scripts.data_augmentation import *
from scripts.model_training import *




#####
###
# 01 Read in images and break them into tiles
###
#####

# set file paths
path = "./data/"
train_path = path + "raw/train/"
val_path = path + "raw/val/"
test_path = path + "raw/test/"
train_tile_path = path + "processed/train_tiles/"
val_tile_path = path + "processed/val_tiles/"
test_tile_path = path + "processed/test_tiles/"
train_save_path = path + "processed/train/"
val_save_path = path + "processed/val/"
test_save_path = path + "processed/test/"
processed_data_dir = path + "processed/"

# Get all the image names in the folders
train_images = os.listdir(train_path)
val_images = os.listdir(val_path)
test_images = os.listdir(test_path)

# Read in the images, store the image and image name
train_images_dict = read_images(train_images)
val_images_dict = read_images(val_images)
test_images_dict = read_images(test_images)

# Break images into tiles
break_images_into_tiles(images_dict=train_images_dict, tile_size=640, overlap=40, tile_path=train_tile_path)
break_images_into_tiles(images_dict=val_images_dict, tile_size=640, overlap=40, tile_path=val_tile_path)
break_images_into_tiles(images_dict=test_images_dict, tile_size=640, overlap=40, tile_path=test_tile_path)




#####
###
# 02 Create augmented data
###
#####

# create rotated images
create_rotated_images(path, path_save=train_save_path)
create_rotated_images(path, path_save=val_save_path)
create_rotated_images(path, path_save=test_save_path)

# create contrast images
create_contrast_images(path, path_save=train_save_path)
create_contrast_images(path, path_save=val_save_path)
create_contrast_images(path, path_save=test_save_path)




#####
###
# 03 Train model
###
#####

# Train the model
model, results, P, R, mAP50, mAP = train_model(processed_data_dir=processed_data_dir, epochs=25)

# Model inference on the test data
test_P, test_R, test_mAP50, test_mAP = model_inference(model, processed_data_dir=processed_data_dir)

# Save the model
model.save("model.pt")