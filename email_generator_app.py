import streamlit as st
import google.generativeai as genai

# Load API Key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Function to generate email using Google Gemini
def generate_email(client_name, client_url, custom_comment):
    prompt = f"""
    Generate a professional sales email for {client_name}. 
    Compliment their achievements based on {client_url}.
    Address their potential AI needs: {custom_comment}.
    Highlight five key benefits of working with Shaip.
    Conclude with a polite request for a meeting.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text if response and hasattr(response, 'text') else "Error generating email."

# Streamlit UI
st.title("AI-Powered Sales Email Generator")

client_name = st.text_input("Client Name")
client_url = st.text_input("Client Website URL")
custom_comment = st.text_area("Custom Requirement")

if st.button("Generate Email"):
    if client_name and client_url and custom_comment:
        email = generate_email(client_name, client_url, custom_comment)
        st.text_area("Generated Email", email, height=300)
        st.download_button("Download Email", email, file_name="sales_email.txt")
    else:
        st.warning("Please fill in all fields.")
