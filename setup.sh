#!/bin/bash
# This script will install dependencies and run the Streamlit app.

# Step 1: Install the Python dependencies
pip install -r requirements.txt

# Step 2: Run the Streamlit app
streamlit run app.py