import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2


def print_unique(data):
	'''
	Show unique values for each column.
	'''
	for col in data.columns:
		uniq = data[col].unique()
		print(f"COLUMN \x1b[1;31m{col}\x1b[0m ({data[col].dtype})")

		# Show first 20 values only
		if len(uniq) > 20:
			print(f'{uniq[:20]}...')
		else:
			print(uniq)
		print()


def count_outliers(data):
	'''
	Get number of outliers for each column.
	Outliers are values outside of the interquantile range.

	Args:
		data: Dataframe where to look for outliers
	Return:
		Dictionary with columnname as key and number of outliers as value
	'''
	d  = {}

	for col in data.select_dtypes(np.number).columns:
		iqr = np.percentile(data[col], 75) - np.percentile(data[col], 25)
		upper_limit = np.percentile(data[col],75) + 1.5*iqr
		lower_limit = np.percentile(data[col],25) - 1.5*iqr
		n_outliers  = data[(data[col] < lower_limit) | (data[col] > upper_limit)].shape[0]

		if n_outliers > 0:
			d[col] = n_outliers
	return d


def get_best_features(X, y, k=10):
	"""
	Get the best k features.

	Args:
	    X: Independent features
	    y: Dependent feature
	    k: Number of features to select
	Return:
	    Dataframe with features and their according score
	"""
	# SelectKBest requires the data to be positive, so we apply
	# a MinMaxScaler before calling it.
	minMax = MinMaxScaler()
	minMax.fit(X, y)
	X_scaled = minMax.transform(X)

	kbest = SelectKBest(chi2, k=k)
	kbest.fit(X_scaled, y)

	ml = [elem for elem in zip(kbest.scores_, X.columns.tolist())]
	ml.sort(reverse=True)
	return pd.DataFrame(data = ml, columns = ['score','feature'])


def get_balanced_data(data, column):
	'''
	Get a dataframe where the unique values of the given column
	are well balanced.

	Args:
		data: The dataset
		column: The column to balance
	Return:
		Balanced dataset
	'''

	if data[column].dtype != object:
		raise Exception('categorical column required')

	balanced = pd.DataFrame()
	nrows = min(data[column].value_counts())

	for val in data[column].value_counts().keys():
		chunk = data[data[column] == val].iloc[:nrows,:].reset_index(drop=True)
		balanced = pd.concat([balanced, chunk], axis=0)

	return balanced
