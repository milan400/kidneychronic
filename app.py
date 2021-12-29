#Basic
import numpy as np
import pandas as pd
import os

# Other libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load Model
import pickle

import streamlit as st 

dirname = os.path.dirname(__file__)

filename = os.path.join(dirname, 'modelandgraph/rfc_high.pkl')


clf = pickle.load(open(filename, 'rb'))


def predict_note_authentication(X):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: Blood Pressure
        in: query
        type: number
        required: true
      - name: Specific Gravity
        in: query
        type: number
        required: true
      - name: Albumin
        in: query
        type: number
        required: true
      - name: Sugar 
        in: query
        type: number
        required: true
      - name: Pus Cell clumps 
        in: query
        type: number
        required: true
      - name: Bacteria 
        in: query
        type: number
        required: true
      - name: Blood Glucose Random 
        in: query
        type: number
        required: true
      - name: Blood Urea 
        in: query
        type: number
        required: true
      - name: Serum Creatinine
        in: query
        type: number
        required: true
      - name: Hemoglobin
        in: query
        type: number
        required: true
      - name: Hypertension
        in: query
        type: number
        required: true
      - name: Diabetes Mellitus
        in: query
        type: number
        required: true   
      - name: Coronary Artery Disease
        in: query
        type: number
        required: true
      - name: Appetite
        in: query
        type: number
        required: true
      - name: Pedal
        in: query
        type: number
        required: true
      - name: Anemia
        in: query
        type: number
        required: true                                    
    responses:
        200:
            description: The output values
        
    """
   
def main():
    st.title("Chronic Kidney Disease Predict")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Chronic Kidney Disease Predict ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.number_input("Age",step=1.,format="%.2f")
    Pressure = st.number_input("Blood Pressure",step=1.,format="%.2f") 
    Gravity= st.number_input("Specific Gravity",step=1.,format="%.2f")
    Albumin= st.number_input("Albumin",step=1.,format="%.2f")
    Sugar = st.number_input("Sugar",step=1.,format="%.2f")
    clumps = st.number_input("Pus Cell clumps",step=1.,format="%.2f")
    Bacteria = st.number_input("Bacteria",step=1.,format="%.2f")
    Glucose = st.number_input("Blood Glucose Random",step=1.,format="%.2f")
    Urea = st.number_input("Blood Urea",step=1.,format="%.2f")
    Serum = st.number_input("Serum Creatinine",step=1.,format="%.2f")
    Hemoglobin = st.number_input("Hemoglobin",step=1.,format="%.2f")
    Hypertension = st.number_input("Hypertension",step=1.,format="%.2f")
    Mellitus = st.number_input("Diabetes Mellitus",step=1.,format="%.2f")
    Coronary = st.number_input("Coronary Artery Disease",step=1.,format="%.2f")
    Appetite= st.number_input("Appetite",step=1.,format="%.2f")
    Pedal= st.number_input("Pedal",step=1.,format="%.2f")
    Anemia= st.number_input("Anemia",step=1.,format="%.2f")

    inpu = [[Age,Pressure, Gravity,Albumin,Sugar,clumps,Bacteria,Glucose ,Urea,Serum,Hemoglobin,Hypertension,Mellitus,Coronary,Appetite,Pedal,Anemia]]

    result=""
    if st.button("Predict"):
        pred=clf.predict(inpu) 

        if(int(pred[0]) != 0):
          result = 'Presence of Kidney Chronic Disease'
        else:
          result='No Presence of Kidney Chronic Disease'

    st.success(result)
    if st.button("About"):
        st.text("Chronic Kidney Disease Predictor")
        st.text("Final Year Project")

if __name__=='__main__':
    main()