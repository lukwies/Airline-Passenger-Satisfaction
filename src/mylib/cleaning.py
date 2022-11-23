import pandas as pd
import numpy as np
import re

def normalize_column_names(data):
	'''
	Normalize column names.
	The following transformations will be applied:

	- Convert all letters to lower case
	- Replace whitespaces with underlines (' ' -> '_')
	- Remove leading/trailing whitespaces, tabs and newlines

	Args:
		Dataframe
	Return:
		Dataframe with normalized column names
	'''
	df = data.copy()
	norm_columns = []

	for col in df.columns:
		colstr = col.strip().lower()
		colstr = re.sub("[\s/-]", "_", colstr)
		norm_columns.append(colstr)

	df.columns = norm_columns

	return df

def drop_nan_rows(data):
	df = data.copy()
	df = df.dropna()
	return df

def clean_gender(data):
	df = data.copy()
	df['gender'] = df['gender'].replace({'Male':'M', 'Female':'F'})
	return df

def clean_customer_type(data):
	df = data.copy()
	df['customer_type'] = df['customer_type'].replace({
		'Loyal Customer':    'Loyal',
		'disloyal Customer': 'Disloyal'})
	return df

def clean_type_of_travel(data):
	df = data.copy()
	df['type_of_travel'] = df['type_of_travel'].replace({
		'Personal Travel': 'Private',
		'Business travel': 'Business'})
	return df


def clean_satisfied(data):
	'''
	Rename column to 'satisfied'.
	Change 'neutral or dissatisfied' to False
	Change 'satisfied' to False
	Change column type to boolean
	'''

	df = data.copy()
	df = df.rename(columns={'satisfaction':'satisfied'})
	df['satisfied'] = df['satisfied'].replace({
		'neutral or dissatisfied': False,
		'satisfied': True})
	return df


def clean_data(data):
	'''
    	Clean the total flight rating dataset.

    	Args:
    	    data: Dataset to clean
    	Return:
    	    Cleaned dataset
	'''
	df = data.copy()
	df = normalize_column_names(df)
	df = drop_nan_rows(df)
	df = clean_gender(df)
	df = clean_customer_type(df)
	df = clean_type_of_travel(df)
	df = clean_satisfied(df)

	return df
