import streamlit as st
import time

# Placeholder function for chat responses
def get_chatbot_response(user_input):
    # Simulate a delay for the chatbot response
    time.sleep(2)  # Simulating processing time
    return f"Chatbot response to: {user_input}"

# Streamlit app layout
st.title("Chatbot")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    with st.spinner("Thinking..."):
        response = get_chatbot_response(user_input)
        st.text_area("Chatbot:", value=response, height=150)
