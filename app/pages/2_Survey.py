import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle
import yaml

from sys import path
import os

path.insert(0, os.path.abspath('../src'))
import mylib.transform as transform


st.set_page_config(
	page_title='Survey',
	page_icon='👋')

st.title("Flight Satisfaction Survey")

with open('../params.yaml') as file:
    config = yaml.safe_load(file)


gender = st.selectbox('Please select your gender', ('Female', 'Male'))
customer_type = st.selectbox('Please select a customer type', ('Loyal', 'Disloyal'))
age = st.number_input('Enter your age', min_value=6, max_value=120, value=35, step=1)
travel_type = st.selectbox('Please select purpose of flight', ('Private', 'Business'))
flight_class = st.selectbox('Please select booked class', ('Eco', 'Eco Plus', 'Business'))
flight_distance = st.number_input('Enter the flight distance', min_value=10, max_value=10000, value=1000, step=10)
rate_wifi = st.slider('How would you rate the inflight wifi service?', 0,5, 3)
rate_time_convenient = st.slider('How convenient was the departure/arrival time?', 0, 5, 3)
rate_online_booking = st.slider('How would you rate the ease of online booking?', 0, 5, 3)
rate_gate_location = st.slider('How would you rate the gate location?', 0, 5, 3)
rate_food = st.slider('How would you rate food and drinking?', 0,5, 3)
rate_online_boarding = st.slider('How would you rate the online boarding?', 0, 5, 3)
rate_seat = st.slider('How would you rate the seat comfort?', 0,5,3)
rate_entertainment = st.slider('How would you rate the inflight entertainment?', 0, 5, 3)
rate_onboard_service = st.slider('How would you rate the onboard service?', 0, 5, 3)
rate_legroom_service = st.slider('How would you rate the legroom service?', 0, 5, 3)
rate_baggage_handling = st.slider('How would you rate the baggage handling?', 0, 5, 3)
rate_checkin_service = st.slider('How would you rate the checkin service?', 0, 5, 3)
rate_inflight_service = st.slider('How would you rate the inflight service?', 0, 5, 3)
rate_cleanliness = st.slider('How would you rate the cleanliness?', 0, 5, 3)
departure_delay = st.number_input('What was the departure delay (in minutes)?', min_value=0, max_value=10000, step=1)
arrival_delay = st.number_input('What was the arrival delay (in minutes)?', min_value=0, max_value=10000, step=1)


# Build dataframe from survey data
def build_dataframe_from_survey_data():
	d = {
		'gender': ['M' if gender=='Male' else 'F'],
		'customer_type': [customer_type],
		'age': [age],
		'type_of_travel': [travel_type],
		'class': [flight_class],
		'flight_distance': [flight_distance],
		'inflight_wifi_service': [rate_wifi],
		'departure_arrival_time_convenient': [rate_time_convenient],
		'ease_of_online_booking': [rate_online_booking],
		'gate_location': [rate_gate_location],
		'food_and_drink': [rate_food],
		'online_boarding': [rate_online_boarding],
		'seat_comfort': [rate_seat],
		'inflight_entertainment': [rate_entertainment],
		'on_board_service': [rate_onboard_service],
		'leg_room_service': [rate_legroom_service],
		'baggage_handling': [rate_baggage_handling],
		'checkin_service': [rate_checkin_service],
		'inflight_service': [rate_inflight_service],
		'cleanliness': [rate_cleanliness],
		'departure_delay_in_minutes': [departure_delay],
		'arrival_delay_in_minutes': [arrival_delay]
	}
	return pd.DataFrame(d)


# Predict satisfaction level
def predict_satisfaction():
	X = build_dataframe_from_survey_data()

	# Load random forest classifier
	with open(config['model']['randForest'], 'rb') as file:
		model = pickle.load(file)

	X = transform.scale_and_encode_unseen(X)
	y_pred = model.predict(X)
#	y_pred_proba = model.predict_proba(X)

#	proba = pd.DataFrame({'True': y_pred_proba[1],
#				'False': y_pred_proba[0]})

	if y_pred[0] == True:
		st.markdown("### Luckily you are satisfied :-)")
	else:
		st.markdown("### Sorry for not being satisfied with our service :-(")

#	st.write(type(y_pred_proba[0][y_pred[0]]))


# Save collected survey data to csv file
def save_survey_to_csv():
	X = build_dataframe_from_survey_data()

	if os.path.isfile(config['data']['survey']):
		df = pd.read_csv(config['data']['survey'])
	else:
		df = pd.DataFrame()

	df = pd.concat([df, X], axis=0)
	df.to_csv(config['data']['survey'], index=False)
	st.write('Saved survey data')


# Buttons
col1, col2, col3, _,_,_ = st.columns(6)
if col1.button('Save'):
	save_survey_to_csv()
if col2.button('Predict'):
	predict_satisfaction()
if col3.button('Reset'):
	st.experimental_rerun()

