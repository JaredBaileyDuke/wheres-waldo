#####
###
# 00 Imports
# 01 Setup
# 02 Screen 0 - Introduction
# 03 Screen 1 - Upload or Select Image
# 04 Screen 2 - Output and Interaction
###
#####




#####
###
# 00 Imports
###
#####
import streamlit as st
import streamlit.components.v1 as components
from PIL import ImageOps, Image
import cv2
import numpy as np
import torch
from ultralytics import YOLO
from src.tiles import *
from src.image_transform import *
from time import sleep




#####
###
# 01 Setup
###
#####
# This loads general code for use by the tool
st.set_page_config(
    page_title="Find Waldo and His Friends Using Computer Vision",
    layout="wide"
)

if 'screen' not in st.session_state:
    st.session_state.screen = 0

if 'image' not in st.session_state:
    st.session_state.image = None

if 'image_counter' not in st.session_state:
    st.session_state.image_counter = 0 

if 'confidence' not in st.session_state:
    st.session_state.confidence = 0.50

if 'model' not in st.session_state:
    st.session_state.model = YOLO("/home/user/app/models/head_model/best.pt")  # load 

_, row0_col1, _ = st.columns([2,3,2])
_, row1_col1, _ = st.columns([2,3,2])
_, row2_col1, _ = st.columns([2,3,2])
_, row3_col1, row3_col2, row3_col3, row3_col4, _ = st.columns([8,3,3,3,3,8])
_, row4_col1, row4_col2, row4_col3, row4_col4, _ = st.columns([8,3,3,3,3,8])
_, row5_col2, row5_col3, row5_col4 = st.columns([1,4,4,1], gap="medium")

# heading
with row0_col1:
    st.markdown("<h1 style='text-align: center; color: black;'>Find Waldo and His Friends</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Using Computer Vision</h3>", unsafe_allow_html=True)



#####
###
# 02 Screen 0 - Introduction
###
#####
# This displays to inform the user about the tool
if st.session_state.screen == 0:
    with row1_col1:
        # overview
        st.markdown("<p style='text-align: left; color: black;'>This tool allows you to take a photo with your phone of a <i>Where's Waldo?</i> book page. Using the computer vision model YOLOv8-large, this tool finds Waldo and his friends Wenda, Odlaw, Wizard, and Woof.</p>", unsafe_allow_html=True)
        
        # purchase option
        st.markdown("<p style='text-align: center; color: black;'><a href='https://www.amazon.com/Wheres-Waldo-Ultimate-Watcher-Collection/dp/1536215112/ref=asc_df_1536215112/?tag=hyprod-20&linkCode=df0&hvadid=496186854683&hvpos=&hvnetw=g&hvrand=13774168920524356768&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9009670&hvtargid=pla-1185030597547&psc=1&mcid=a517c47662b13f96a80fbf3bfe8b30fe&gclid=CjwKCAjwuJ2xBhA3EiwAMVjkVADBaOb87R0kxhnpKqL-S_gJWme0DJJAwSTe-VlUv2p19zZKak3cshoCR34QAvD_BwE'>Purchase the Books</a></p>", unsafe_allow_html=True)
        
        # email          
        st.markdown("<p style='text-align: center; color: black;'><a href=mailto:'Jared.L.Bailey@duke.edu'>Jared.L.Bailey@duke.edu</a></p>", unsafe_allow_html=True) 
        
        # proceed button
        _, row1a_col1, _ = st.columns([2,1,2])
        with row1a_col1:
            if st.button("Proceed", key="Proceed", use_container_width=True):
                st.session_state.screen = 1 
                st.rerun()

        # image of Waldo and his friends
        st.image("/home/user/app/home_page_images/Waldo_Friends.jpg", use_column_width=True)

        
 
       
    
    
#####
###
# 03 Screen 1 - Upload or Select Image
###
#####
if st.session_state.screen == 1:  
    # heading and instructions
    with row1_col1:
        st.markdown("<p style='text-align: center; color: black;'>Upload an image using your cell phone (single book page), or select an image from the below list</p>", unsafe_allow_html=True)

    # image uploader
    with row2_col1:
        uploaded_image = st.file_uploader(label="", 
                                          type=['jpg'], 
                                          accept_multiple_files=False, 
                                          key=None, 
                                          help='Due to image resolution limitations of the tool, only photos of a single page are expected to produce the intended result', 
                                          on_change=None, 
                                          args=None, 
                                          kwargs=None, 
                                          disabled=False, 
                                          label_visibility="visible"
                                          )
        if uploaded_image is not None:
            uploaded_image = Image.open(uploaded_image)
            uploaded_image = ImageOps.exif_transpose(uploaded_image)
            st.session_state.image = uploaded_image
            st.session_state.screen = 2
            st.rerun()

        # image selector
        st.markdown("<h4 style='text-align: center; color: black;'>Or Select One of the Following</h4>", unsafe_allow_html=True)
    
    image_path = "/home/user/app/test_images/"
    with row3_col1:
        img_1 = image_transform("IMG_5356.JPG", image_path)
        st.image(img_1, use_column_width=True)
        if st.button("Select Image ↑", key="button_1", use_container_width=True):
            st.session_state.image = img_1
            st.session_state.screen = 2
            st.rerun()
    with row3_col2:
        img_2 = image_transform("IMG_5357.JPG", image_path)
        st.image(img_2, use_column_width=True)
        if st.button("Select Image ↑", key="button_2", use_container_width=True):
            st.session_state.image = img_2
            st.session_state.screen = 2
            st.rerun()
    with row3_col3:
        img_3 = image_transform("IMG_5368.JPG", image_path)
        st.image(img_3, use_column_width=True)
        if st.button("Select Image ↑", key="button_3", use_container_width=True):
            st.session_state.image = img_3
            st.session_state.screen = 2
            st.rerun()
    with row3_col4:
        img_4 = image_transform("IMG_5369.JPG", image_path)
        st.image(img_4, use_column_width=True)
        if st.button("Select Image ↑", key="button_4", use_container_width=True):
            st.session_state.image = img_4
            st.session_state.screen = 2
            st.rerun()
    with row4_col1:
        img_5 = image_transform("IMG_5382.JPG", image_path)
        st.image(img_5, use_column_width=True)
        if st.button("Select Image ↑", key="button_5", use_container_width=True):
            st.session_state.image = img_5
            st.session_state.screen = 2
            st.rerun()
    with row4_col2:
        img_6 = image_transform("IMG_5383.JPG", image_path)
        st.image(img_6, use_column_width=True)
        if st.button("Select Image ↑", key="button_6", use_container_width=True):
            st.session_state.image = img_6
            st.session_state.screen = 2
            st.rerun()
    with row4_col3:
        img_7 = image_transform("IMG_5408.JPG", image_path)
        st.image(img_7, use_column_width=True)
        if st.button("Select Image ↑", key="button_7", use_container_width=True):
            st.session_state.image = img_7
            st.session_state.screen = 2
            st.rerun()
    with row4_col4:
        img_8 = image_transform("IMG_5409.JPG", image_path)
        st.image(img_8, use_column_width=True)
        if st.button("Select Image ↑", key="button_8", use_container_width=True):
            st.session_state.image = img_8 
            st.session_state.screen = 2
            st.rerun()

#####
###
# 04 Screen 2 - Output and Interaction
###
#####      
if st.session_state.screen == 2:  
    # tile images
    st.session_state.tiles = tile_image(image=st.session_state.image, tile_size=640, overlap=40)

    with row5_col2:
        st.session_state.boxed_image = np.array(st.session_state.image)
        height, width, channels = st.session_state.boxed_image.shape
        st.session_state.blank_img = np.zeros((height + 640, width + 640, 3), np.uint8)
        st.session_state.blank_img[0:height, 0:width] = st.session_state.boxed_image

        counter = 1
        for i in range(0, width, 600):
            for j in range(0, height, 600):
                # draw the rectangle
                cv2.rectangle(st.session_state.blank_img, (i, j), (i + 640, j + 640), (0, 255, 0), 10)
                # add the number of the rectangle
                cv2.putText(st.session_state.blank_img, str(str(counter)), (i + 200, j + 320), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 10)
                counter += 1  
        st.image(st.session_state.blank_img, use_column_width=True) 
    
    with row5_col3:
        # navigation
        row5a_col0, row5a_col1, row5a_col2= st.columns([1,1,1], gap="large")
        with row5a_col0:
            if st.button("Back", use_container_width=True):
                if st.session_state.image_counter > 0:
                    st.session_state.image_counter -= 1
        with row5a_col1:
            if st.button("Select New Photo", use_container_width=True):
                st.session_state.screen = 1
                st.session_state.results = None
                st.session_state.image_counter = 0
                st.rerun()
        with row5a_col2:
            if st.button("Next", use_container_width=True):
                if st.session_state.image_counter < len(st.session_state.results) - 1:
                    st.session_state.image_counter += 1

        # predictions
        if 'results' not in st.session_state or st.session_state.results == None:
            st.write("\n\n")
            st.markdown("<p style='text-align: center; color: black;'>The model is working. Please be patient...</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: black;'>This process can take up to 30 seconds.</p>", unsafe_allow_html=True)
            st.session_state.results = st.session_state.model.predict(st.session_state.tiles, conf=st.session_state.confidence) # predict     
            st.rerun()

        with row5_col4:
            # show character locations
            class_names = {0: "Waldo", 1: "Wenda", 2: "Odlaw", 3: "Wizard", 4: "Woof"}
            character_dict = {
                "Waldo": [],
                "Wenda": [],
                "Odlaw": [],
                "Wizard": [],
                "Woof": [],
            }
            for idx, pred in enumerate(st.session_state.results):
                try:
                    for boxes in pred.boxes:
                        if boxes.conf >= 0.5:
                            character_dict[class_names[int(boxes.cls.item())]].append(idx + 1)
                except:
                    pass
                    
            st.session_state.output = "  \n\n\n\n\n  Tile Numbers:  \n"
            for key, value in character_dict.items():
                if value != []:
                    st.session_state.output += str(key) + ": "+ str(value) + "  \n"
    
            st.write(st.session_state.output)
            
        # plot predicted image
        st.markdown(f"<h4 style='text-align: center; color: black;'>Image Tile {str(st.session_state.image_counter + 1)}</h4>", unsafe_allow_html=True)
        im_bgr = st.session_state.results[st.session_state.image_counter].plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image
        st.image(im_rgb)