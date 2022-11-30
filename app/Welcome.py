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
	page_title='Welcome',
	page_icon=''
)

#st.sidebar.success('Select a page')


st.markdown('# Analysis on Flight Rating')
st.markdown('by Lukas Wiese')
st.write("")
st.markdown('<img width="500" src="https://cdn.cnn.com/cnnnext/dam/assets/210810173434-4-pan-am-707-economy-meals-credit-anne-sweeney-full-169.jpg">', unsafe_allow_html=True)
st.write("")
st.markdown('''
	An airline company is interested in how passengers rate their flight and aviation service.
	Therefore they envolved a survey to figure out the satisfaction level of their customers.
	Now that airline hired us for analysing the data to get better insights of the survey results.
	For a detailed description of the dataset, [click here](#dataset-description).
	'''
)
st.markdown('## Business Questions')
st.markdown('''
    	- What is the average rating of the airline services?
    	- Which services are rated best and which one worst?
    	- Is there a difference in the rating between males and females?
    	- What impact has the flightclass on the rating ?
    	- Is the rating worse on longer flight distance?
    	- Do passengers rate better on private than on business flights?
    	- Does the age of a customer effect the rating?
	''')

st.markdown('## Dataset Description')
st.markdown('''
	<table>
	<tr><th>Column Name</th><th>Value Range</th></tr>
	<tr><td>Id</td><td>1-129880</td></tr>
	<tr><td>Gender</td><td>Male, Female</td></tr>
	<tr><td>Customer Type</td><td>Loyal, Disloyal</td></tr>
	<tr><td>Age</td><td>7-85</td></tr>
	<tr><td>Type of Travel</td><td>Private, Business</td></tr>
	<tr><td>Class</td><td>Economic, Economic Plus, Business</td></tr>
	<tr><td>Flight Distance</td><td>31-4983km</td></tr>
	<tr><td>Inflight wifi service</td><td>0-5</td></tr>
	<tr><td>Departure/Arrival time convenient</td><td>0-5</td></tr>
	<tr><td>Ease of online booking</td><td>0-5</td></tr>
	<tr><td>Gate location</td><td>0-5</td></tr>
	<tr><td>Food and drink</td><td>0-5</td></tr>
	<tr><td>Online boarding</td><td>0-5</td></tr>
	<tr><td>Seat comfort</td><td>0-5</td></tr>
	<tr><td>Inflight entertainment</td><td>0-5</td></tr>
	<tr><td>Onboard service</td><td>0-5</td></tr>
	<tr><td>Leg room service</td><td>0-5</td></tr>
	<tr><td>Baggage handling</td><td>0-5</td></tr>
	<tr><td>Checkin service</td><td>0-5</td></tr>
	<tr><td>Inflight service</td><td>0-5</td></tr>
	<tr><td>Cleanliness</td><td>0-5</td></tr>
	<tr><td>Departure Delay in Minutes</td><td>0-1592 min</td></tr>
	<tr><td>Arrival Delay in Minutes</td><td>0-1584 min</td></tr>
	<tr><td>satisfaction</td><td>neutral or dissatisfied, satisfied</td></tr>
	</table>
	''', unsafe_allow_html=True)
