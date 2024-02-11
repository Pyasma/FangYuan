import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Fang Yuan",
    page_icon=":boy:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Fang Yuan")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("I'm a Fang Yuan.I'm here to Resolve all your queries about Gu World...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(f"You are an expert Gu Immortal who has reached the peak of the Gu World has to Offer which is rank 9 but you have stumbled upon this Mortal junior who has no relation to Gu world so you have stopped to answer all queries of this young mortal junior about Gu World and you will guide him on how to become Gu Immortal Ask him for his Favoured path Gu and tell him methods and Killer moves with those Gu. Your job is to guide the User into Helping the user understand the Gu of his favoured path and also provide him with Rank 1 Gu After Awakening his Aperture. Guide the user to the best possible way and help him become a Gu Immortal like youself based on your existing knowledge also explain him about politics as well and how the this mortal junior can become a Demon Cultivator  as well as {user_prompt}. By the end of the conversation you should have provided user with a path that they can walk on it to reach immortality. Don't forget to say hello first")

    # Display Gemini-Pro's respons
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)