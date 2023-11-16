import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import re
import pickle

st.set_page_config(layout="wide")

st.write("""
<div style='text-align:center'>
    <h1 style='color:#009999;'>Retail Sales Prediction Application</h1>
</div>
""", unsafe_allow_html=True)

selected_tab = st.sidebar.selectbox("Select Tab", ["PREDICTED SALES"])

if selected_tab == "PREDICTED SALES":
    # Define the possible values for the dropdown menus
    Store_options = list(range(1, 46))
    Dept_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 58, 59, 60, 67, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    Isholiday_options = [False, True]
    Size_options = [151315, 202307, 37392, 205863, 34875, 202505, 70713, 155078, 125833, 126512, 207499, 112238, 219622, 200898, 123737, 57197, 93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107, 152513, 204184, 206302, 93638, 42988, 203750, 203007, 39690, 158114, 103681, 39910, 184109, 155083, 196321, 41062, 118221]
    Month_options = list(range(1, 13))
    Year_options = [2010, 2011, 2012, 2013]

    # Define the widgets for user input
    with st.form("my_form"):
        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            st.write(' ')
            Store = st.selectbox("Store", Store_options, key=1)
            Dept = st.selectbox("Dept", Dept_options, key=2)
            IsHoliday = st.selectbox("IsHoliday", Isholiday_options, key=3)
            Size = st.selectbox("Size", Size_options, key=4)
            Month = st.selectbox("Month", Month_options, key=5)
            Year = st.selectbox("Year", Year_options, key=6)
        with col3:
            st.write(
                f'<h5 style="color:rgb(0, 153, 153,0.4);">NOTE: Min & Max given for reference, you can enter any value</h5>',
                unsafe_allow_html=True)
            MarkDown1 = st.text_input("Enter MarkDown1 (Min: -2780 & Max:103185)")
            MarkDown2 = st.text_input("Enter MarkDown2 (Min: -265 & Max:104520)")
            MarkDown3 = st.text_input("Enter MarkDown3 (Min: -180 & Max:149485)")
            MarkDown4 = st.text_input("Enter MarkDown4 (Min: 0.22 & Max:67475)")
            MarkDown5 = st.text_input("Enter MarkDown5 (Min: -185 & Max:771445)")
            submit_button = st.form_submit_button(label="PREDICTED SALES")
            st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #009999;
                        color: white;
                        width: 100%;
                    }
                    </style>
                """, unsafe_allow_html=True)

        flag = 0
        pattern = "^(?:\d+|\d*\.\d+)$"
        # Validation code for input fields
        for i in [MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5]:
            if re.match(pattern, i):
                pass
            else:
                flag = 1
                break

        if submit_button and flag == 1:
            if len(i) == 0:
                st.write("please enter a valid number space not allowed")
            else:
                st.write("You have entered an invalid value: ", i)

        if submit_button and flag == 0:
            # Create input data DataFrame
            data = {
                'Store': [Store],
                'Dept': [Dept],
                'IsHoliday': [IsHoliday],
                'Size': [Size],
                'Month': [Month],
                'Year': [Year],
                'MarkDown1': [float(MarkDown1)],
                'MarkDown2': [float(MarkDown2)],
                'MarkDown3': [float(MarkDown3)],
                'MarkDown4': [float(MarkDown4)],
                'MarkDown5': [float(MarkDown5)]
            }
            input_data = pd.DataFrame(data)

            # Load the model from the pickle file
            with open("model.pkl", 'rb') as file:
                loaded_model = pickle.load(file)

            # Encoding 'IsHoliday' using LabelEncoder
            label_encoder = LabelEncoder()
            input_data['IsHoliday'] = label_encoder.fit_transform(input_data['IsHoliday'])

            # Prepare input data for prediction
            new_sample = input_data.values  # Use input_data directly as an array

            # Make predictions
            try:
                new_pred = loaded_model.predict(new_sample)
                st.write('## :red[Predicted sales:] ', (new_pred))
            except Exception as e:
                st.write('Error occurred during prediction:', str(e))

st.write(f'<h6 style="color:rgb(0, 153, 153,0.35);">App Created by Nivash K </h6>', unsafe_allow_html=True)

