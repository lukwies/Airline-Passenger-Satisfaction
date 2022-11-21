import pandas as pd
import numpy as np
import yaml
import pickle
import sys

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, PowerTransformer, MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor

import lib.cleaning as clean


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
	df = data.copy().drop(['date', 'daytime', 'seasons',
			'functioning_day', 'temperature_type',
			'solar_radiation'], axis=1)

	X = df.drop(['rented_bike_count'], axis=1)
	y = df['rented_bike_count']
	return X,y


def encode_and_scale(config, X, y):
	'''
	Apply encoder and scalers to given X/y columns.

	Args:
		config: YAML config instance
		X: Dependent columns
		y: Independent column
	Return:
		X, y
	'''
	with open(config['encoder']['onehot'], 'rb') as file:
		ohe = pickle.load(file)

	X_cat     = X.select_dtypes(object)
	X_cat_enc = ohe.transform(X_cat).toarray()
	X_cat_enc = pd.DataFrame(X_cat_enc, columns=ohe.get_feature_names_out())


	with open(config['scaler']['standard'], 'rb') as file:
		standard = pickle.load(file)

	X_num        = X.select_dtypes(np.number)
	X_num_scaled = standard.transform(X_num)
	X_num_scaled = pd.DataFrame(X_num_scaled, columns=X_num.columns)


	with open(config['scaler']['minmax'], 'rb') as file:
		minmax = pickle.load(file)

	X_num_scaled = minmax.transform(X_num_scaled)
	X_num_scaled = pd.DataFrame(X_num_scaled, columns=X_num.columns)


	X = pd.concat([X_cat_enc, X_num_scaled], axis=1)

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

	with open(config['model']['KNN'], 'rb') as file:
		knn = pickle.load(file)

	y_pred = knn.predict(X)
	score  = knn.score(X, y)

	return y_pred,score



if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Please pass a bike-sharing dataset for performing the prediction!!")
		sys.exit()

	with open('../params.yaml') as file:
		config = yaml.safe_load(file)

	df = load_and_clean_data(sys.argv[1])

	X,y = split_X_y(df)
	X,y = encode_and_scale(config, X, y)

	y_pred,score = apply_model(config, X, y)

	print(f"Score: {score}")
	print("y-predicted:")
	print(y_pred)
