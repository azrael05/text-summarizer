import streamlit as st
from trans_sum import get_summary
from tinydb import TinyDB

# Initialize chat history
db = TinyDB('chat_history.json')

st.title("Text Summarizer")
# file = st.file_uploader("Pick a file")

# Initialize chat history from previous sessions
chat_history = db.all()
# Check if 'key' already exists in session_state
# If not, then initialize it
for message in chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    user_message = {"role": "user", "content": prompt}
    chat_history.append(user_message)
    db.insert(user_message)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner(text="In progress..."):
        response = get_summary(prompt)[0]["summary_text"]
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    # Add assistant response to chat history
    assistant_message = {"role": "assistant", "content": response}
    chat_history.append(assistant_message)
    db.insert(assistant_message)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Reset chat history button
if len(db.all()) > 0:
    # Show button if Chat history not empty
    if st.button("Reset Chat"):
        # Delete all entries in Database
        db.truncate()
        # Reload Page
        st.experimental_rerun()