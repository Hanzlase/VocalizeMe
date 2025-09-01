import streamlit as st
import os
import requests
import time
import docx
import PyPDF2
from dotenv import load_dotenv
import tempfile

# Load environment variables
load_dotenv()

# Resemble AI Configuration
RESEMBLE_API_KEY = os.getenv("RESEMBLE_API_KEY")
RESEMBLE_VOICE_UUID = os.getenv("RESEMBLE_VOICE_UUID")
RESEMBLE_PROJECT_UUID = os.getenv("RESEMBLE_PROJECT_UUID")

# Streamlit app
st.title("Text to Speech Converter with Resemble AI")
st.write("Upload a DOC or PDF file to convert its text to speech in your custom voice.")

# File uploader
uploaded_file = st.file_uploader("Choose a DOC or PDF file", type=["doc", "docx", "pdf"])

# Temporary file paths
output_audio_path = os.path.join(tempfile.gettempdir(), "converted_audio.wav")

def extract_text_from_doc(file):
    """Extract text from a DOC/DOCX file."""
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs if para.text])

def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def convert_text_to_speech(text):
    """Convert text to speech using Resemble AI and return the audio file path."""
    clip_uuid = None
    try:
        # Step 1: Call Resemble AI API with the text
        st.write("Calling Resemble AI to start conversion...")
        api_url = f"https://app.resemble.ai/api/v2/projects/{RESEMBLE_PROJECT_UUID}/clips"
        headers = {
            'Authorization': f'Token {RESEMBLE_API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            "voice_uuid": RESEMBLE_VOICE_UUID,
            "body": text,
            "title": "Converted Clip"
        }

        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        if data.get('success'):
            clip_uuid = data['item']['uuid']
            st.write(f"API call successful! Your new clip UUID is: {clip_uuid}")
        else:
            st.error(f"API Error after call: {data.get('message', 'Unknown error')}")
            return None

    except requests.exceptions.HTTPError as err:
        st.error(f"HTTP Error calling Resemble AI API: {err}")
        st.error(f"Response from server: {err.response.text}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred during API call: {e}")
        return None

    # Step 2: Poll for results and download
    if clip_uuid:
        st.write("Waiting for conversion to finish...")
        clip_url = f"https://app.resemble.ai/api/v2/projects/{RESEMBLE_PROJECT_UUID}/clips/{clip_uuid}"
        audio_src_url = None
        max_retries = 30

        for i in range(max_retries):
            try:
                poll_headers = {'Authorization': f'Token {RESEMBLE_API_KEY}'}
                response = requests.get(clip_url, headers=poll_headers)
                response.raise_for_status()
                data = response.json()

                if data.get('item') and data['item'].get('audio_src'):
                    audio_src_url = data['item']['audio_src']
                    st.write("Conversion finished!")
                    break
                else:
                    st.write(f"Status check ({i+1}/{max_retries}): Not ready yet...")
                    time.sleep(2)
            except requests.exceptions.HTTPError as err:
                st.error(f"HTTP Error while checking status: {err}")
                return None

        if not audio_src_url:
            st.error("Timed out: The conversion took too long.")
            return None

        # Step 3: Download the converted audio with authentication
        st.write("Downloading converted audio...")
        try:
            audio_response = requests.get(audio_src_url, headers={'Authorization': f'Token {RESEMBLE_API_KEY}'})
            audio_response.raise_for_status()

            with open(output_audio_path, 'wb') as f:
                f.write(audio_response.content)
            
            st.write(f"Success! Converted audio saved to '{output_audio_path}'")
            return output_audio_path

        except requests.exceptions.HTTPError as err:
            st.error(f"HTTP Error during download: {err}")
            st.error(f"Response from server: {err.response.text}")
            return None

if uploaded_file is not None:
    # Extract text based on file type
    file_extension = uploaded_file.name.split(".")[-1].lower()
    try:
        if file_extension in ["doc", "docx"]:
            text = extract_text_from_doc(uploaded_file)
        elif file_extension == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a DOC, DOCX, or PDF file.")
            text = None

        if text:
            st.write("### Extracted Text:")
            st.text_area("Text Content", text, height=200)
            
            if st.button("Convert to Speech"):
                audio_file = convert_text_to_speech(text)
                if audio_file:
                    st.audio(audio_file, format="audio/wav")
                    with open(audio_file, "rb") as file:
                        st.download_button(
                            label="Download Converted Audio",
                            data=file,
                            file_name="converted_audio.wav",  # Fixed filename
                            mime="audio/wav"
                        )

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a file to proceed.")