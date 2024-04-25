# model training code attribution (YouTube Handle): Computer Vision Engineer
# YouTube: https://www.youtube.com/watch?v=m9fH9OWn8YM&t=2078s

#####
###
# 00 Imports
###
#####
from ultralytics import YOLO
import os



#####
###
# 01 Train Model
###
#####
def train_model(processed_data_dir, epochs=25):
    """
    Train the YOLO model on the processed data.
    
    Args:
        - processed_data_dir: str, the path to the processed data directory (must contain images, labels, and data.yaml)
        - epochs: int, the number of epochs to train the model

    Returns:
        - model: YOLO, the trained YOLO model
        - results: dict, the results of the training
        - P: float, the precision of the model
        - R: float, the recall of the model
        - mAP50: float, the mean average precision at 50 of the model
        - mAP: float, the mean average precision (50-95) of the model
    """
    # Load the model
    model = YOLO("yolov8l.yaml")

    # Train the model
    results = model.train(data=os.path.join(processed_data_dir, "data.yaml"), epochs=epochs)

    # Get the model metrics
    metrics = model.val()

    return (model, results, metrics.P.val, metrics.R.val, metrics.map50.val, metrics.map.val)




#####
###
# 02 Model Inference
###
#####
def model_inference(model, processed_data_dir):
    """
    Perform inference on the test data using the trained model.
    And save the images with the bounding boxes drawn around the objects.

    Args:
        - model: YOLO, the trained YOLO model
        - processed_data_dir: str, the path to the processed data directory (must contain images, labels, and data.yaml)

    Returns:
        - P: float, the precision of the model
        - R: float, the recall of the model
        - mAP50: float, the mean average precision at 50 of the model
        - mAP: float, the mean average precision (50-95) of the model
    """
    # Save the results of the model inference
    # A separate folder will automatically be created
    results = model.predict(source=os.path.join(processed_data_dir, "images/test"), save=True)

    # Get the model metrics
    metrics = model.val()

    return (metrics.P.test, metrics.R.test, metrics.map50.test, metrics.map.test)
