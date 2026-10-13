import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="CloudSense AI", page_icon="☁️", layout="centered")

st.title("☁️ CloudSense: Serverless Sentiment Analyzer")
st.write("A zero-cost, cloud-native application running entirely on PaaS and Serverless infrastructure.")

# User Input Section
user_text = st.text_area("Enter customer review or feedback text:", "The cloud deployment was seamless and fast!")

if st.button("Analyze Sentiment in Cloud"):
    if user_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Sending request to cloud serverless model..."):
            # Using a public Hugging Face zero-cost serverless model endpoint
            API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
            
            payload = {"inputs": user_text}
            
            try:
                response = requests.post(API_URL, json=payload)
                result = response.json()
                
                # Parse and display results
                if isinstance(result, list) and len(result) > 0:
                    predictions = result[0]
                    st.success("Analysis Complete!")
                    for item in predictions:
                        label = item.get("label")
                        score = item.get("score") * 100
                        st.metric(label=f"Sentiment: {label}", value=f"{score:.2f}%")
                else:
                    st.error("Received unexpected response from cloud endpoint. Please try again.")
            except Exception as e:
                st.error(f"Cloud connection error: {e}")
