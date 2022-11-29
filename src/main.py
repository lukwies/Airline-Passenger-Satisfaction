import pandas as pd
import numpy as np
import yaml
import pickle
import sys

from sklearn.model_selection import train_test_split

import mylib.cleaning as clean
import mylib.transform as trans

def load_and_clean_data(csv_path):
	'''
	Load dataset from csv-file and clean it.
	Args:
		csv_path: Path to csv file
	Return:
		Cleaned dataset
	'''
	df = pd.read_csv(csv_path)
	return clean.clean_data(df)


def split_X_y(data):
	'''
	Split data into independent and dependent columns.
	Args:
		data: Dataframe to split
	Return:
		X, y
	'''
	X = df.drop(['id', 'satisfied'], axis=1)
	y = df['satisfied']
	return X,y


def apply_model(config, X, y):
	'''
	Load and apply the KNeighborRegression model.
	Args:
		config: YAML config instance
		X: Dependent columns
		y: Independent column
	Return:
		y_pred,score
	'''

	with open(config['model']['randForest'], 'rb') as file:
		rF = pickle.load(file)

	y_pred = rF.predict(X)
	score  = rF.score(X, y)

	return y_pred,score



if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Please pass a flight rating dataset for performing the prediction!!")
		sys.exit()

	with open('../params.yaml') as file:
		config = yaml.safe_load(file)

	df = load_and_clean_data(sys.argv[1])

	X,y = split_X_y(df)
	X   = trans.scale_and_encode_unseen(X)
	y_pred,score = apply_model(config, X, y)

	print(f"Score: {score}")
	print("y-predicted:")
	print(y_pred)
