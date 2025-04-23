import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = joblib.load('vectorizer.pkl')
resp_vecs = joblib.load('resp_vecs.pkl')
df = pd.read_csv('df_match.csv')

