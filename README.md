# Where's Waldo
Find Waldo and His Friends Using Computer Vision

![Image](https://github.com/JaredBaileyDuke/wheres-waldo/blob/main/images/Waldo_Friends.jpg)

## Streamlit App
### Available on HuggingFace
https://huggingface.co/spaces/JaredBailey/WheresWaldo

### Run locally
```bash
streamlit run streamlit/app.py
```

## Introduction
### Problem
Where's Waldo is an illustrated children's book containing a challenge: Can the reader find Waldo and his friends in a series of very complex illustrations? 

The challenge is difficult because of the large size of the illustrations, the small size of the desired characters, and frequent obstructions in front of the desired characters. As seen in the image above, Waldo's friends have a many similarities, adding to the challenge.

### Past Work
Many people have attempted to find Waldo in the past, but not his friends. As well, past attempts focused on using high resolution images in near perfect lighting conditions. There are several common datasets used frequently amongst these projects. There is also a project using a robot with imperfect lighting to point to Waldo with a rubber hand. This robot makes use of high resolution photography.

A few links to these projects:
- https://medium.com/@reece.riherd_73510/can-a-computer-answer-wheres-waldo-using-machine-learning-to-find-waldo-362ee674fb3f
- https://medium.com/analytics-vidhya/finding-waldo-using-a-simple-convolutional-neural-network-1604cb4d2e55
- https://github.com/arrufat/wallyfinder
- https://www.businessinsider.com/wheres-waldo-robot-ai-machine-learning-2019-2#check-out-theres-waldo-in-action-below-9

### Objective
This project set out to have the user find Waldo using a cell phone camera. This made the problem increasingly difficult as it the model learned from a real-life setting with curved pages and imperfect lighting conditions. 

## Training
### Data
#### Overview
The data was gathered using an iPhone X. The images are of single pages of the book, as capturing 2 pages at one time was too low a resolution for the model to handle.

The images were tiled to allow for input to the model without the reducing the image size to 640x640 and thereby losing valuable pixels. The tiles were given overlaps of 40 pixels to help reduce the chance that a character would be split across multiple tiles and missed by the model.

Images were then augmented to allow for rotation at 90, 180, and 270 degrees. This simulated a phone not always taking a photo at the desired rotation when used from above and pointing down at the book. As well, images were given contrast to simulate different lighting conditions.

#### Storage
The data is too large to store in this repo, even in a zip file format. The data has been stored in a Box folder, and access can be granted as requested.

### Modeling
#### Process
Modeling was perform with Google Colab and the use of a Google TPU. 2 notebooks are provided in the notebooks folder showcasing the work (One searching for character heads and one for character heads + bodies). The final model chosen was the head model as it performed better. Despite the additional pixel size of the bounding boxes for the head + body model, the frequent body obstructions in the illustrations created difficulty for the model to learn the character patterns.

The setup.py file allows for users to process the data, train the model, perform inference on the test data, and save out the results. Several helper scripts are provided in the scripts folder to assist.
- tiling.py - for splitting the raw images into their individual tiles of 640x640 pixels with overlaps of 40 pixels between tiles
- data_augmentation.py - for rotating images (since phone cameras sometimes rotate images in surprising ways to the user) and increasing the image contrast (50% brighter and 50% darker) to simulate different lighting conditions
- model_training.py - for training the model using ultralytics (with inference on validation data), performing inference on the test data, saving the test images with predicted bounding boxes, gathering evaluation metrics, and saving the model

The setup.py file can be run from the command line.
```bash
python setup.py
```

#### Naive Model
As models were not trained on the characters of Waldo and his friends, the models do not have a way of identifying them. This results in Naive YOLOv8 model that produces 0 predictions.

#### Non-Deep Learning Approach
Non-deep learning approaches are not viable for this problem. This is due to several reasons.
- Classical models such as tree based and GLMs predict a single number. They do not predict 4 points to make a bounding box, classification, and confidence score all at once as a deep learning model can.
- In non-deep learning approaches images must be flattened in order to form a feature table. As these characters are quite small and move from picture to picture, the predictive columns are therefore different from illustration to illustration. This makes learning impossible as no feature has a chance to learn on more than one illustration.
- The data size is wildly large to be handled by a classical model (640x640 pixels over 3 channels for 2,300+ images). The use of convolutional layers makes training possible with today's computing resources.