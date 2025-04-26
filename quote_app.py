import pandas as pd
import streamlit as st
import random

# Load the quotes
df = pd.read_csv("quotes.csv")

# Page setup
st.set_page_config(page_title="Mood-Based Quote Generator", page_icon="💬")
st.title("✨ Quote Generator for Your Mood")
st.write("Enter how you're feeling and receive a quote that speaks to your heart 💛")

# Mood input
mood = st.text_input("How are you feeling today? (e.g. hopeful, tired, anxious)")

# Button to generate quote
if st.button("Get Quote"):
    if mood:
        mood_lower = mood.strip().lower()
        filtered = df[df['mood'].str.lower() == mood_lower]
        if not filtered.empty:
            quote = random.choice(filtered['quote'].tolist())
            st.success(f"💬 *{quote}*")
        else:
            st.warning("I don't have a quote for that mood yet, but you're doing amazing. 💛")
    else:
        st.warning("Please type in a mood first 😊")

# Optional: Add a random quote button
if st.button("Surprise Me! 🎲"):
    quote = random.choice(df['quote'].tolist())
    st.info(f"💬 *{quote}*")
