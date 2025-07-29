import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('House Price Prediction')

st.write('Enter the house features to get a price prediction.')

# Create input fields for the features
gr_liv_area = st.slider('Above ground living area (square feet)', 334, 5642, 1500)
bedroom_abv_gr = st.slider('Number of bedrooms above ground', 0, 8, 3)
full_bath = st.slider('Number of full bathrooms', 0, 3, 2)

# Create a button to make predictions
if st.button('Predict Price'):
    # Prepare the input data for the model
    input_data = np.array([[gr_liv_area, bedroom_abv_gr, full_bath]])

    # Make the prediction
    predicted_price = model.predict(input_data)

    # Display the prediction
    st.write(f'The predicted house price is: ${predicted_price[0]:,.2f}')
