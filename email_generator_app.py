import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key="AIzaSyBsk4bbenI5DAeixex6eVNYmCGB5w5Hazk")  # Replace with your actual API Key

# Function to generate email using Gemini AI
def generate_email(client_url, client_name, custom_comment):
    prompt = f"""
    Generate a professional email introducing Shaip to {client_name}.
    The email should include:
    - A personalized compliment based on {client_name}'s company website: {client_url}
    - Shaip’s AI annotation services and expertise
    - Five benefits of working with Shaip
    - A polite request for availability

    Additional details: {custom_comment}
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit Web App Interface
st.title("AI-Powered Email Generator ✉️")

# Input fields
client_url = st.text_input("Client Website URL:")
client_name = st.text_input("Client Contact Name:")
custom_comment = st.text_area("Custom Requirement (Optional):")

# Generate email on button click
if st.button("Generate Email"):
    if client_url and client_name:
        email_text = generate_email(client_url, client_name, custom_comment)
        st.text_area("Generated Email:", email_text, height=300)

        # ✅ Use Streamlit’s built-in copy functionality with a download button
        st.download_button(label="Copy & Download Email", data=email_text, file_name="generated_email.txt", mime="text/plain")
        
    else:
        st.error("Please enter both Client URL and Contact Name.")
