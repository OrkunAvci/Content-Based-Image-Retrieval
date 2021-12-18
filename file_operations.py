import cv2 as cv
from os import listdir
from os.path import isfile, join
import json

folders = [
	#   Img sets to use
	"octopus",
	"elephant",
	"flamingo",
	"kangaroo",
	"leopards",
	"sea_horse"
]

files = [f for f in listdir("./data/camera") if isfile(join("./data/camera", f))]   #   Get all file names
train_file_names = files[:20]   #   First 20 is train
test_file_names = files[20:30]  #   Next 10 is test

def get_train_set():
	img_set = [[cv.imread("./data/" + folder + "/" + file_name) for file_name in train_file_names] for folder in folders]
	return img_set

def get_test_set():
	img_set = [[cv.imread("./data/" + folder + "/" + file_name) for file_name in test_file_names] for folder in folders]
	return img_set

def save(file_name, data):
	with open("./data/" + file_name, "w+") as f:
		f.write(json.dumps(data))

def read(file_name):
	with open("./data/" + file_name, "r+") as f:
		return json.loads(f.read())