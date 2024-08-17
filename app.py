import streamlit as st

# Set page title
st.set_page_config(page_title="Simple Streamlit App", page_icon="🚀")

# Add a title
st.title("Welcome to My Simple Streamlit App")

# Add some text
st.write("This is a basic Streamlit application.")

# Add a sidebar
st.sidebar.header("Sidebar")
st.sidebar.write("You can add controls here.")

# Create a text input
user_input = st.text_input("Enter your name:", "")

# Create a button
if st.button("Say hello"):
    if user_input:
        st.write(f"Hello, {user_input}!")
    else:
        st.write("Please enter your name.")

# Add a slider
number = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")

# Display a chart
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)

# Add a footer
st.markdown("---")
st.write("Thanks for using this simple Streamlit app!")
