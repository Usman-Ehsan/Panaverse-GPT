import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

# Streamlit Page Configuration
st.set_page_config(page_title="Panaverse Chatbot", layout="centered")

# Title
st.title("📄 Panaverse AI-Powered Chatbot")

api_key = "AIzaSyC3avmgebf2--Ygi5TAYMyfpb4G2ciyFoY"

if api_key:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
    
        
    loader = PyPDFLoader("document.pdf")
    pages = loader.load_and_split()
    document = loader.load()
        
        # User Input
    user_input = st.text_input("Ask Anything You Want To Know:")
if st.button("Submit"):   
    if user_input:
            prompt = f"""
                You have to respond to the user query{user_input} based on the provided document.{document}
                
                If the user query is not from the document, respond with "Sorry, I am unable to answer that question."
            """
            
            response = llm.invoke(prompt)
            st.subheader("Response:")
            st.write(response.content)
    else:
        st.warning("Please enter a question before submitting.")

