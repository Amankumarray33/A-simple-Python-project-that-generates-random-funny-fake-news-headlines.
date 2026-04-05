import streamlit as st
import random

subjects = ["Aliens","Politician","Dog","Student","Teacher"]
actions = ["launches","eats","destroys","creates","discovers"]
places = ["in Delhi","on Mars","inside a classroom","at a tea stall","in Bihar"]

def generate_headline():
    return f"{random.choice(subjects)} {random.choice(actions)} {random.choice(places)} 😂"

st.title("📰 Fake News Generator")

if st.button("Generate Headline"):
    st.success(generate_headline())
