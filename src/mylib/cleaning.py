import pandas as pd
import numpy as np
import re

def normalize_column_names(columns):
	'''
	Normalize column names.
	The following transformations will be applied:

	- Convert all letters to lower case
	- Replace whitespaces with underlines (' ' -> '_')
	- Remove leading/trailing whitespaces, tabs and newlines

	Args:
		columns: List of column names
	Return:
		List of normalized columns
	'''
	norm_columns = []

	for col in columns:
		colstr = col.strip().lower()
		colstr = re.sub("[\s/-]", "_", s)
		norm_columns.append(colstr)

	return norm_columns


def adjust_column_types(data):
	'''
    	Change datatype of column "date" to pd.datetime64.

    	Args:
        	data: Dataframe
    	Return:
        	Cleaned dataframe
	'''
	df = data.copy()
	df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')

	return df


def change_holiday_values(data):
	'''
    	Changes values of the column holiday.

    	  "Holiday"    -> "Yes"
    	  "No Holiday" -> "No"

    	Args:
    	    data: Dataset to clean
    	Return:
    	    Cleaned dataset
	'''
	df = data.copy()
	df['holiday'] = df['holiday'].replace({'Holiday':'Yes', 'No Holiday':'No'})

	return df


def add_daytime_column(data):
	'''
    	Creates a new column "daytime" depending on column "hour".
    	Values of the new column can be Morning, Noon, Afternoon, Evening or Night.

    	  hour 4 to 10  -> Morning
    	  hour 11 to 14 -> Noon
    	  hour 15 to 17 -> Afternoon
    	  hour 18 to 21 -> Evening
    	  hour 22 to 3  -> Night

    	Args:
        	data: Dataframe to add column to
    	Return:
        	New dataframe
	'''
	def get_time_of_day(hour):
		if hour >= 4 and hour < 11:
			return "Morning"
		elif hour >= 11 and hour < 15:
			return "Noon"
		elif hour >= 15 and hour < 18:
			return "Afternoon"
		elif hour >= 18 and hour < 22:
			return "Evening"
		else:
			return "Night"
	df = data.copy()
	df['daytime'] = df['hour'].apply(get_time_of_day)

	return df


def add_weekday_column(data):
	'''
    	Creates a new column "weekday" depending on column "date".

    	Args:
        	data: Dataframe to add column to
    	Return:
        	Updated dataframe
	'''
	df = data.copy()
	df['weekday'] = df['date'].dt.weekday

	return df


def add_temperature_type_column(data):
	'''
    	Creates a new column "temperature_type" depending on column "temperature".
    	Values of the new column can be Hot, Warm, Mild, Cold or Frost.

    	  temp > 30  -> Hot
    	  temp 20-30 -> Warm
    	  temp 10-20 -> Mild
    	  temp 0-10  -> Cold
    	  temp < 0   -> Frost

    	Args:
    	    data: Dataframe to add column to
    	Return:
    	    New dataframe
	'''
	def get_temperature_type(temp):
		if temp > 30:
			return "Hot"
		elif temp > 20 and temp <= 30:
			return "Warm"
		elif temp > 10 and temp <= 20:
			return "Mild"
		elif temp >= 0 and temp <= 10:
			return "Cold"
		else:
			return "Frost"

	df = data.copy()
	df['temperature_type'] = df['temperature'].apply(get_temperature_type)

	return df


def add_month_column(data):
	'''
    	Creates a new column with the month extracted from column date.
    	Args:
    	    data: Dataframe to add column to
    	Return:
    	    New dataframe
	'''
	df = data.copy()
	df['month'] = pd.DatetimeIndex(df['date']).month

	return df


def reorder_columns(data):
	'''
    	Reorder columns for a better overview.
    	Args:
    	    data: Dataframe
    	Return:
    	    Dataframe with different column order
	'''
	df = data.copy()
	return df[['date', 'month', 'hour', 'daytime', 'weekday',
		'seasons', 'holiday', 'functioning_day',
		'temperature', 'temperature_type',
		'humidity', 'wind_speed', 'visibility',
		'solar_radiation', 'rainfall', 'snowfall',
		'rented_bike_count']]


def clean_data(data):
	'''
    	Clean the total bike sharing dataset.

    	Args:
    	    data: Dataset to clean
    	Return:
    	    Cleaned dataset
	'''
	df = data.copy()
	df.columns = normalize_column_names(df)
	df = adjust_column_types(df)
	df = change_holiday_values(df)
	df = add_weekday_column(df)
	df = add_daytime_column(df)
	df = add_temperature_type_column(df)
	df = add_month_column(df)
	df = reorder_columns(df)

	return df
