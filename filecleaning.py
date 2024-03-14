import tensorflow as tf
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import pathlib
from PIL import Image
import numpy
import os
import sys

train_dir = pathlib.Path(r'C:\Users\ethan\Downloads\mandarin_images\new_test\final_images\CASIA-HWDB_Train\Train')
test_dir = pathlib.Path(r'C:\Users\ethan\Downloads\mandarin_images\new_test\final_images\CASIA-HWDB_Test\Test')

def get_image_files(directory):
    """
    Recursively find all image files within a directory and its subdirectories.
    """
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                image_files.append(os.path.join(root, file))
    return image_files

train_image_files = get_image_files(train_dir)

def check_for_empty_images(image_files):
    """
    Check a list of image files for images that could cause the 'Input is empty' error during decoding.
    """
    problematic_images = []
    for image_file in image_files:
        try:
            image = tf.io.read_file(image_file)
            image = tf.io.decode_image(image)
            if image.shape[0] == 0 or image.shape[1] == 0:
                problematic_images.append(image_file)
        except Exception as e:
            print(f"Error processing {image_file}: {e}")
            problematic_images.append(image_file)
    return problematic_images

train_problematic = check_for_empty_images(train_image_files)
print (train_problematic)