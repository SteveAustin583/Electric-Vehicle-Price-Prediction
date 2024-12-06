import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib
from flask import Flask, render_template
# Environment
# , FileSystemLoader
# , PackageLoader, select_autoescape
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

# Load the pre-trained model (make sure to save your model from the notebook)
model = joblib.load('model/ev_price_model.pkl')

def predict_price(features):
    # Preprocess the features
    # For simplicity, assume you have transformed your dataset in the same way as in the notebook.
    
    # OneHotEncoder or preprocessing steps as in your notebook
    encoder = joblib.load('model/encoder.pkl')  # Load encoder if needed
    
    features_df = pd.DataFrame([features], columns=['County', 'City', 'ZIP Code', 'Model Year', 'Make', 'Model', 'Electric Vehicle Type', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility', 'Legislative District'])
    
    # Apply encoding, scaling, etc., if necessary
    transformed_features = encoder.transform(features_df)
    
    # Make the prediction
    price = model.predict(transformed_features)
    
    return price[0]  # Assuming it returns a single value
