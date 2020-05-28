#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf 
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import json
from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', default="/test_images/orchid.jpg")
parser.add_argument('model', action="store", default="my_model.h5")
parser.add_argument ("--top_k", help="define top k", type=int)
parser.add_argument("-category_names", help="category names directory", type=int)
args = parser.parse_args()


def process_image(image_array):
    
    image_tf = tf.convert_to_tensor(image_array)
    image_tf.shape.as_list() 
    image_tf = tf.image.resize(image_tf, size=[224, 224])
    image_tf /= 255.0
    return image_tf.numpy()

def predict(image_path, model, top_k):
    im = Image.open(image_path)
    im = np.asarray(im)
    image = process_image(im)
    image = image.reshape((1, 224, 224, 3))
    probs = model.predict(image)[0]
    best_index = np.argsort(probs)[::-1][:(top_k)]
    probs = probs[best_index]
    best_classes = [str(x+1) for x in best_index]
    return probs, best_classes


image_path = args.path
saved_keras_model_filepath = args.model
if isinstance(args.top_k, int):
    top_k = args.top_k
else:
    top_k = 5
    
if isinstance(args.category_names, str):
    map_file = args.category_names
else:
    map_file = 'label_map.json'

with open(map_file) as handle:
    class_names = json.loads(handle.read())

model = tf.keras.models.load_model(saved_keras_model_filepath, custom_objects={'KerasLayer':hub.KerasLayer})

probs, classes = predict(image_path, model, top_k)
im = Image.open(image_path)
im = np.asarray(im)
image = process_image(im)

fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
ax1.imshow(image, cmap = plt.cm.binary)
ax1.axis('off')
ax2.barh(np.arange(top_k), probs)
ax2.set_aspect(0.1)
ax2.set_yticks(np.arange(top_k))
top_k_labels = [class_names[x] for x in classes]
ax2.set_yticklabels(top_k_labels, size='small')
ax2.set_title('Class Probability')
ax2.set_xlim(0, 1.1)
plt.tight_layout()
plt.show()
