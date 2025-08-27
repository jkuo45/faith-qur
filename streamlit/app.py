from streamlit_searchbox import st_searchbox

import streamlit as st

st.title("Chat with Text")

# Chapter selection
chapters = [
    "Chapter 01: The Creation and Fall of Man",
    "Chapter 02-08: (Elihu, Truth, Sinful Ways, abbv.)",
    "Chapter 20: Holy Instructions and Warnings for All Young Men",
    "Chapter 21: Marriage Instructions for Man and Wife",
    "Chapter 22: Duty of a Husband",
    "Chapter 26: Holy Instructions on Unity",
    "Chapter 30: Social Duties",
    "Chapter 31: Justice",
    "Chapter 33: Gratitude",
    "Chapter 34: Sincerity",
    "Chapter 36: Know Thyself",
    "Chapter 37: The Breath of Heaven",
    "Chapter 38: The Soul of Man",
    "Chapter 40: The Instability of Man",
    "Chapter 43: Insufficiency of Knowledge",
    "Chapter 44: Misery",
    "Chapter 46: The Beginning of Christianity",
]

selected_chapter = st_searchbox(
    label="Select chapters",
    placeholder="Search...",
    default_options=chapters,
    search_function=[],
)


# Chat interface
user_input = st.chat_input("Ask a question about the chapter")

if user_input:
    st.write(f"You asked: {user_input}")
    st.write("This is a placeholder response.")
