# Content Based Image Retrieval

## Data

http://www.vision.caltech.edu/Image_Datasets/Caltech101/

## Quickstart

Uncomment https://github.com/OrkunAvci/Content-Based-Image-Retrieval/blob/ae4841c9f2c71a4c903d3dade9065e1ac9ae5c7d/main.py#L32 this line. It will generate the storage.

You can configure the list of folders in `file_manipulations.py` for customs tests. Be sure to run `start_up()` every time you want to overwrite stored data.

There are 60 images per folder in original data but only half of it is used here. First 20 as training and next 10 as testing. You can customize these numbers in `file_manipulations.py`.

## What is this?

In simplest terms, homework. In more complex terms, a program to create histograms(RGB & HSV) out of images into training and testing data sets and find top 5 most similar images in `train` for each image in `test`.
