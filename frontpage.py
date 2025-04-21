import streamlit as st
import csv
import pandas as pd

st.title("Welcome to the Front Page")
st.header("Data Input")
number = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
st.write(f"You entered: {number}")
if number == 51:
    st.success("You entered the secret number!")
else:
    st.error("That's not the secret number.")
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("Enter your name:")
with c2:
    message = st.text_input("Enter your message:")
row = [name, message]
if st.button("Submit"):
    with open("messages.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    st.success("Your message has been submitted!")
    st.balloons()

df = pd.read_csv("messages.csv", names=["Name", "Message"])
st.write(df)
st.audio_input(label="Say something")
