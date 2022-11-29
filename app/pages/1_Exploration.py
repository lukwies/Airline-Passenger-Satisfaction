import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time
import yaml

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


# All rating columns
rate_cols = ['inflight_wifi_service', 'departure_arrival_time_convenient',
		'ease_of_online_booking', 'gate_location', 'food_and_drink',
		'online_boarding', 'seat_comfort', 'inflight_entertainment',
		'on_board_service', 'leg_room_service', 'baggage_handling',
		'checkin_service', 'inflight_service', 'cleanliness']
# All rating column labels
rate_cols_labels = ['Wifi service', 'Departure/Arrival time convenient',
		'Ease of online booking', 'Gate location', 'Food and drink',
		'Online boarding', 'Seat comfort', 'Inflight entertainment',
		'Onboard service', 'Leg room service', 'Baggage handling',
		'Checkin service', 'Inflight service', 'Cleanliness']


with open('../params.yaml') as file:
	config = yaml.safe_load(file)


st.set_page_config(
	page_title='Exploration',
	page_icon='👋')


st.title("Flight Ratings Exploration")

data = pd.read_csv(config['data']['explore'])


# Plot average rating by flight class
def plot_ratings_by_flight_class():

	grp = data.pivot_table(index='class', values='rating_avg').reset_index()

	fig = px.bar(grp, x='class', y='rating_avg', color='class',
		color_discrete_map={'Business':'#6699ff', 'Eco':'#0055ff', 'Eco Plus':'#003cb3'})
	fig.update_layout(xaxis_title='Flight class',
			yaxis_title='Average Rating',
			title='Rating by flight class')
	st.plotly_chart(fig, use_container_size=True)


# Plot average rating by age
def plot_rating_by_age():

	grp = data.pivot_table(index='age', values=rate_cols).reset_index()

	fig = go.Figure()
	fig.update_xaxes(title_text='Age')
	fig.update_yaxes(title_text='Rating')
	fig.update_layout(title='Ratings by age')

	for col,lbl in zip(rate_cols, rate_cols_labels):
		fig.add_trace(go.Scatter(x=grp['age'], y=grp[col],
			mode='lines', name=lbl))

	st.plotly_chart(fig, use_container_width=True)


# Rating by Flight Distance
def plot_rating_by_flight_distance():
	grp = data.pivot_table(index='flight_distance_class', values='rating_avg').reset_index()

	fig = px.bar(grp, x='flight_distance_class', y='rating_avg', color='flight_distance_class',
		color_discrete_map={'short':'#b3ffb3', 'medium':'#33ff33', 'long':'#00b300'})
	fig.update_layout(xaxis_title='Flight distance',
			yaxis_title='Average Rating',
			title='Rating by flight distance')
	st.plotly_chart(fig, use_container_size=True)


# Best/Worst Ratings
def plot_best_worst_features():
	d = {}
	for col in rate_cols:
		d[col] = [data[col].mean()]

	grp = pd.DataFrame(d).T.sort_values(by=0).reset_index()
	grp.columns = ['feature', 'rating']

	fig = px.bar(grp, y='rating', x='feature', color='feature')
	fig.update_layout(yaxis_title='Average Rating', xaxis_title='',
			title='Best/Worst features', height=600)
	st.plotly_chart(fig, use_container_size=False)

def plot_overall_rating_ditribution():
	fig = px.histogram(data, x='rating_avg')
	fig.update_layout(yaxis_title='', xaxis_title='Rating',
			title='Overall Rating')
	st.plotly_chart(fig, use_container_size=True)


plot_overall_rating_ditribution()
plot_best_worst_features()
plot_ratings_by_flight_class()
plot_rating_by_flight_distance()
plot_rating_by_age()
