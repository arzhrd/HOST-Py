import streamlit as st

st.title("🔢 Simple Addition App")

# Take user inputs
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# Calculate and display result
sum_result = num1 + num2
st.success(f"The sum is: {sum_result}")
