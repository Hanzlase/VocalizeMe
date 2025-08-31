<div align="center">

# 🎤 VOCALIZEME

### *Turn Your Documents Into Your Own Voice*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_Now-6366f1?style=for-the-badge)](https://vocalizeme.streamlit.app/)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/vocalizeme?style=for-the-badge&color=gold)](https://github.com/yourusername/vocalizeme/stargazers)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![ResembleAI](https://img.shields.io/badge/Resemble_AI-Voice_Cloning-purple?style=flat-square)
![Deployment](https://img.shields.io/badge/Deployed_on-Streamlit_Cloud-FF4B4B?style=flat-square&logo=streamlit)

</div>

---

## 🎯 What is VocalizeMe?

**VocalizeMe** is a next-generation **document-to-voice application** that transforms text from **PDFs and Word documents** into **realistic speech in your own cloned voice**.  
With seamless integration of **Resemble AI** and a simple **Streamlit interface**, it’s never been easier to bring your documents to life.  

> 🎓 **Perfect for**: Students, educators, audiobook creators, professionals, and anyone who wants to *hear* their written content in their own voice.  

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 📂 **Input Support**
- 📄 Upload **DOC/DOCX** files
- 📑 Upload **PDF** documents
- 📝 Automatic text extraction
- ⏳ Real-time progress tracking

</td>
<td width="50%">

### 🔊 **Output Magic**
- 🎙️ Convert text to **realistic speech**
- 🧑‍🎤 Use your **own cloned voice** (Resemble AI)
- 💾 Download speech as **.wav**
- 🎧 Play audio directly in the app

</td>
</tr>
</table>

---

## 🛠️ Technology Stack

<div align="center">

### **Core Technologies**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

### **Libraries**
![python-docx](https://img.shields.io/badge/python--docx-Document_Parsing-blue?style=for-the-badge)
![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF_Extraction-green?style=for-the-badge)
![requests](https://img.shields.io/badge/requests-HTTP-orange?style=for-the-badge)
![dotenv](https://img.shields.io/badge/python--dotenv-Env_Vars-yellow?style=for-the-badge)

### **Voice AI**
![ResembleAI](https://img.shields.io/badge/Resemble_AI-Voice_Cloning-purple?style=for-the-badge)

</div>

---

## 🚀 Quick Start

### 📋 Prerequisites

```bash
✅ Python 3.9+ installed
✅ Resemble AI API key
✅ Streamlit account (for deployment)
⚡ Installation
bash
Copy code
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/vocalizeme.git
cd vocalizeme

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Create a .env file and add your keys
echo "RESEMBLE_API_KEY=your_api_key" >> .env
echo "RESEMBLE_VOICE_UUID=your_voice_uuid" >> .env
echo "RESEMBLE_PROJECT_UUID=your_project_uuid" >> .env

# 4️⃣ Run the app
streamlit run app.py
📖 How to Use
🎯 Upload a file (DOCX or PDF)

🔍 Preview extracted text inside the app

🎙️ Click "Convert to Speech"

🎧 Listen to the output directly in the browser

💾 Download the generated audio in .wav format

🏗️ Project Structure
bash
Copy code
vocalizeme/
├── app.py               # Main Streamlit app
├── requirements.txt     # Dependencies
├── .env.example         # Example environment variables
├── README.md            # Documentation (you are here)
└── output/              # Generated audio files
🔑 Environment Variables
Create a .env file in the root directory:

env
Copy code
RESEMBLE_API_KEY=your_resemble_api_key
RESEMBLE_VOICE_UUID=your_voice_uuid
RESEMBLE_PROJECT_UUID=your_project_uuid
🌐 Deployment
VocalizeMe is live on Streamlit Cloud:
👉 Visit App

Deploy Yourself:
Push your code to GitHub

Go to Streamlit Cloud

Select your repo → branch → app.py

Add environment variables in Secrets Manager

Deploy 🎉

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

<div align="center">
⭐ Star this repo if you love VocalizeMe!


Made with ❤️ using Streamlit & Resemble AI
Bring your documents to life in your own voice.

</div> ```
