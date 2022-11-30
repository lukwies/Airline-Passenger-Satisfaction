import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle

from sys import path
import os

path.insert(0, os.path.abspath('../src'))
import mylib.transform as transform


st.set_page_config(page_title='Data', page_icon='', layout='wide')
st.title("Flight Satisfaction Survey Data")


if os.path.isfile('../data/survey/survey.csv'):
	df = pd.read_csv('../data/survey/survey.csv')
	st.write(df)
	if st.button('Clear data'):
		os.remove('../data/survey/survey.csv')
		st.experimental_rerun()
else:
	st.write("No data collected yet")


