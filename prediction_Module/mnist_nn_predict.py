from keras.models import model_from_json
from PIL import Image
import numpy as np
import itertools
import os
import keras

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
modelpath = 'prediction_Module/trained_models/'

def loadModel(modelpath):
	# Load the architecture of model
	json_file = open(modelpath+"model.json","r")
	model_json = json_file.read()
	json_file.close()
	model = model_from_json(model_json)

	# Load the weights
	model.load_weights(modelpath+"model.h5")

	return model

def predict_nn(img):
	model = loadModel(modelpath)
	img = img.reshape(1,img.shape[0],img.shape[1],1)
	label = model.predict_classes(img)[0]
	keras.backend.clear_session()

	return label

def preprocess(image_path):
	print(image_path)
	RATIO=2
	img = Image.open(image_path)
	img_arr = np.asarray(img)
	x = img_arr.shape[0]
	y = img_arr.shape[1]

	img = np.asarray(img.resize((int(x/RATIO),int(y/RATIO)))) # a 2D array
	img = img/255.

	return img

# This function will be called from Django website with argument as the image path
def predict(image_path, clf='NN'):

	img = preprocess(image_path)

	if clf == 'NN':
		label = predict_nn(img)
	
	return label    # The output should be a json with "name of the file, label predicted and confidence value. "
