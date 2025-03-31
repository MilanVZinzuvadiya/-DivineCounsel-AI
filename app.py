import streamlit as st
import random
import time
from response import get_christ_res
st.set_page_config(
    page_title="Divine Counsel",
    page_icon="✝️",
    menu_items={
        'About': "A Christian RAG-based AI for Mental Health Guidance DivineCounsel-AI is a Retrieval-Augmented Generation (RAG) system designed to provide mental health guidance rooted in Christian faith. It leverages biblical scriptures, theological insights, and the Word of God to offer comfort, wisdom, and encouragement."
    }
)
st.subheader("✝️ Divine Counsel ✝️")
hide_streamlit_style = """
<style>
.stAppToolbar {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Greetings! \n\n Uncover the meanings behind the parables in the Bible with me."}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "user":
        # Display user message in chat message container
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"], avatar="✝️"):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Seek wisdom, ask freely." ):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        #st.text(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant",avatar="✝️"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner("Praying...🙏🙏🙏"):
            assistant_response = get_christ_res(prompt, st.session_state.messages)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split("\n"):
            for c in chunk:
              full_response += c
              time.sleep(0.01)
              # Add a blinking cursor to simulate typing
              message_placeholder.markdown(full_response + "▌")
            full_response += "\n"
        message_placeholder.markdown(assistant_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
