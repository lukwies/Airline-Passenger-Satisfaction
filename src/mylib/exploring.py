import pandas as pd
import numpy as np


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
