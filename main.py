import numpy as np

import file_operations as fo
import image_manipulations as im

previously_ran_code = """
train = fo.get_train_set()

rgb = []
hsv = []
for group in train:
	for img in group:
		rgb.append(im.get_rgb(img))
		hsv.append(im.get_hsv(img))

fo.save("train_rgb", rgb)
fo.save("train_hsv", hsv)

test = fo.get_test_set()

rgb = []
hsv = []
for group in test:
	for img in group:
		rgb.append(im.get_rgb(img))
		hsv.append(im.get_hsv(img))

fo.save("test_rgb", rgb)
fo.save("test_hsv", hsv)
"""

train_rgb = fo.read("train_rgb")
train_hsv = fo.read("train_hsv")

test_rgb = fo.read("test_rgb")
test_hsv = fo.read("test_hsv")

for test_index in range(len(test_rgb)):
	similarity_dict = {}
	for train_index in range(len(train_rgb)):
		similarity_dict[train_index] = np.linalg.norm( np.array(test_rgb[test_index]) - np.array(train_rgb[train_index]) )
	similarity_dict = {k: v for k, v in sorted(similarity_dict.items(), key=lambda item: item[1], reverse = True)}
	print(dict(list(similarity_dict.items())[:5]))
	