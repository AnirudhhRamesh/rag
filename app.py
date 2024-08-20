import streamlit as st

# Set page title
st.set_page_config(page_title="Chat with your docs", page_icon="�")

# Add a title
st.title("Chat with your docs [WIP]")

# Add some text
st.write("RAG system built from scratch with support for multiple models (OpenAI, Anthropic, Groq)")

st.write("Still a WIP, need to implement DB first.")

# Add link to GitHub repository
st.markdown("View the codebase on [GitHub](https://github.com/anirudhhramesh/rag)")

