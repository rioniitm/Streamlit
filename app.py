import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome"

def main():
  st.title("Subtraction")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Subtraction of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  result = num1 - num2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("RION DSILVA")
      st.text("21f1000930")

if __name__=='__main__':
  main()
