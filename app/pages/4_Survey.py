import streamlit as st
import pandas as pd
import numpy as np
import time
#
# Run with:
# $ streamlit run app.py
#

#st.write("Here's our first attempt at using data to create a table:")


#add_selectbox = st.sidebar.selectbox(
#	"How would you like to be contacted?",
#	("Email", "Home phone", "Mobile phone")
#)
#if st.sidebar.button('Push me'):
#	st.sidebar.write('Hello World')


st.set_page_config(
	page_title='Survey',
	page_icon='👋'
)


st.title("Flight Satisfaction Survey")



gender = st.selectbox('Please select your gender', ('Female', 'Male'))
customer_type = st.selectbox('Please select a customer type', ('Loyal', 'Disloyal'))
age = st.number_input('Enter your age', min_value=6, max_value=120, value=35, step=1)
travel_type = st.selectbox('Please select purpose of flight?', ('Private', 'Business'))
flight_class = st.selectbox('Please select booked class?', ('Economy', 'Economy Plus', 'Business'))
flight_distance = st.number_input('Enter the flight distance', min_value=10, max_value=10000, value=1000, step=10)
rate_wifi = st.slider('How would you rate the inflight wifi service?', 0,5)
rate_time_convenient = st.slider('How convenient was the departure/arrival time?', 0, 5)
rate_ease_booking = st.slider('How would you rate the ease of online booking?', 0, 5)
rate_gate_location = st.slider('How would you rate the gate location?', 0, 5)
rate_food = st.slider('How would you rate food and drinking?', 0,5)
rate_online_boarding = st.slider('How would you rate the online boarding?', 0, 5)
rate_seat = st.slider('How would you rate the seat comfort?', 0,5)
rate_entertainment = st.slider('How would you rate the inflight entertainment?', 0, 5)
rate_onboard_service = st.slider('How would you rate the onboard service?', 0, 5)
rate_legroom_service = st.slider('How would you rate the legroom service?', 0, 5)
rate_baggage_handling = st.slider('How would you rate the baggage handling?', 0, 5)
rate_checkin_service = st.slider('How would you rate the checkin service?', 0, 5)
rate_inflight_service = st.slider('How would you rate the inflight service?', 0, 5)
rate_cleanliness = st.slider('How would you rate the cleanliness?', 0, 5)
departure_delay = st.number_input('What was the departure delay (in minutes)?', min_value=0, max_value=10000, step=1)
arrival_delay = st.number_input('What was the arrival delay (in minutes)?', min_value=0, max_value=10000, step=1)




#'You selected: ', rate_wifi

if st.button('Submit'):
	chart_data = pd.DataFrame(
		np.random.randn(20, 3),
		columns=['a', 'b', 'c'])

	st.line_chart(chart_data)
	st.write("...")
