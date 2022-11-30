import streamlit as st
import pandas as pd
import numpy as np
import time
import yaml
import pickle

from sys import path
import os

path.insert(0, os.path.abspath('../src'))
import mylib.transform as transform

# Load configs
with open('../params.yaml') as file:
	config = yaml.safe_load(file)


st.set_page_config(page_title='Data', page_icon='', layout='wide')
st.title("Flight Satisfaction Survey Data")


if os.path.isfile(config['data']['survey']):
	df = pd.read_csv(config['data']['survey'])
	st.write(df)
	if st.button('Clear data'):
		os.remove(config['data']['survey'])
		st.experimental_rerun()
else:
	st.write("No data collected yet")


