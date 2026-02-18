import pandas as pd

#Load the metadata
metadata = pd.read_csv("./data/group_data/metadata.csv")
metadata

# print all images

# import libraries
import os
import matplotlib.pyplot as plt
import numpy as np

#count 10 images
count = 0

#choose 10 random

while count < 117:

    # all ID's and paths
    pa_index = count
    le_id = str(metadata.at[pa_index , "lesion_id"])
    im_id = str(metadata.at[pa_index , "img_id"])
    dir_path = './data/group_data/metadata.csv'
    img_dir = "./data/group_data/imgs/"
    mask_dir = "./data/group_data/masks/"

    #making mask id
    img_to_mask = metadata.at[pa_index , "img_id"]
    split_mask = img_to_mask.split(".")
    mask_id = split_mask[0] + "_mask"

    # chosen patients information

    # path for image
    im_filename = f"{im_id}"
    im_path = os.path.join(img_dir, im_filename)

    # path for mask
    mask_filename = f"{mask_id}.png"
    mask_path = os.path.join(mask_dir, mask_filename)

    # making subplot
    fig = plt.figure()
    im = plt.imread(im_path)
    ax1 = fig.add_subplot(2,2,1)
    ax1.imshow(im)
    mask = plt.imread(mask_path)
    ax2 = fig.add_subplot(2,2,2)
    ax2.imshow(mask)

    # removing axes
    ax1.set_axis_off()
    ax2.set_axis_off()

    # adding titles
    ax1.title.set_text('Image')
    ax2.title.set_text('Mask')
    fig.suptitle(f"Patient: {metadata.at[pa_index , "img_id"]}, diagnostic: {metadata.at[pa_index , "diagnostic"]}")

    count += 1
