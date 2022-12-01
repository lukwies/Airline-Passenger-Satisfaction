import pandas as pd
import numpy as np
import yaml
import pickle

from sklearn.preprocessing import StandardScaler, PowerTransformer, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder



def scale_and_encode(X_train, X_test, store_as_pickle=True):
	'''
	Applies PowerTransformer, StandardScaler and OneHotEncoder
	on given train and test set. All scalers/encoders are stored
	as a pickle file:
		PowerTransformer -> ../scaler/power_transformer.pkl
		StandardScaler -> ../scaler/standard_scaler.pkl
		OneHotEncoder -> ../encoder/onehot.pkl

	Args:
		X_train: Training set
		X_test:  Testing set
	Return:
		X_train, X_test: Scaled and encoded
	'''

	# Load yaml config
	with open('../params.yaml') as file:
		config = yaml.safe_load(file)

	# Split into numerical and categorical
	X_train_num = X_train.select_dtypes(np.number)
	X_test_num  = X_test.select_dtypes(np.number)

	X_train_cat = X_train.select_dtypes(object)
	X_test_cat  = X_test.select_dtypes(object)

	# Apply PowerTransformer
	pT = PowerTransformer()
	pT.fit(X_train_num)

	X_train_num_np = pT.transform(X_train_num)
	X_test_num_np  = pT.transform(X_test_num)

	if store_as_pickle:
		with open(config['scaler']['power'], 'wb') as file:
			pickle.dump(pT, file)

	# Apply StandardScaler
	sS = StandardScaler()
	sS.fit(X_train_num_np)

	X_train_num_np = sS.transform(X_train_num_np)
	X_test_num_np  = sS.transform(X_test_num_np)

	if store_as_pickle:
		with open(config['scaler']['standard'], 'wb') as file:
			pickle.dump(sS, file)

	# Apply OneHotEncoder
	ohe = OneHotEncoder(drop='first')
	ohe.fit(X_train_cat)

	X_train_cat_np = ohe.transform(X_train_cat).toarray()
	X_test_cat_np  = ohe.transform(X_test_cat).toarray()

	if store_as_pickle:
		with open(config['encoder']['onehot'], 'wb') as file:
			pickle.dump(ohe, file)


	X_train_num = pd.DataFrame(X_train_num_np, columns=X_train_num.columns)
	X_test_num  = pd.DataFrame(X_test_num_np, columns=X_test_num.columns)

	X_train_cat = pd.DataFrame(X_train_cat_np, columns=ohe.get_feature_names_out())
	X_test_cat  = pd.DataFrame(X_test_cat_np, columns=ohe.get_feature_names_out())


	# Build scaled/encoded train/test set dataframes
	X_train = pd.concat([X_train_num, X_train_cat], axis=1)
	X_test = pd.concat([X_test_num, X_test_cat], axis=1)

	return X_train, X_test



def scale_and_encode_unseen(X):
	'''
	Load fitted PowerTransformer, StandardScaler and OneHotEncoder
	from pickle file and apply each of them to the given X values.

	Args:
		X: Dataset to scale
	Return:
		Scaled and encoded dataset
	'''

	# Load yaml config
	with open('../params.yaml') as file:
		config = yaml.safe_load(file)

	# Split into numerical and categorical
	X_num = X.select_dtypes(np.number)
	X_cat = X.select_dtypes(object)

	# Apply PowerTransformer
	with open(config['scaler']['power'], 'rb') as file:
		pT = pickle.load(file)
	X_num_np = pT.transform(X_num)

	# Apply StandardScaler
	with open(config['scaler']['standard'], 'rb') as file:
		sS = pickle.load(file)
	X_num_np = sS.transform(X_num_np)

	# Apply OneHotEncoder
	with open(config['encoder']['onehot'], 'rb') as file:
		ohe = pickle.load(file)
	X_cat_np = ohe.transform(X_cat).toarray()

	X_num = pd.DataFrame(X_num_np, columns=X_num.columns)
	X_cat = pd.DataFrame(X_cat_np, columns=ohe.get_feature_names_out())

	# Build scaled/encoded train/test set dataframes
	return pd.concat([X_num, X_cat], axis=1)

