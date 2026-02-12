# 🤖 Smart YouTube Comment Analyzer

A Machine Learning powered web application that analyzes YouTube comments in real-time. It uses **Natural Language Processing (NLP)** to determine sentiment, classifies comments into categories (Spam, Question, Appreciation), and generates an AI-powered summary of viewer feedback.

## 🚀 Features
- **📊 Sentiment Analysis:** Classifies comments as Positive, Negative, or Neutral.
- **🧠 Machine Learning Classifier:** Automatically tags comments as "Question", "Appreciation", or "Spam".
- **📝 AI Summarization:** Generates a concise paragraph summary of the entire comment section.
- **📈 Visual Analytics:** Displays sentiment distribution using interactive charts.
- **🌑 Dark Mode UI:** Modern, responsive React interface.

## 🛠️ Tech Stack
- **Frontend:** React.js, Chart.js, CSS3
- **Backend:** Python, Flask, TextBlob
- **AI/ML:** Scikit-learn (Naive Bayes), Hugging Face Transformers
- **API:** Google YouTube Data API v3

## ⚙️ Installation Guide

### 1. Clone the Reposotory
git clone [https://github.com/Pranshu475/smart-youtube-analyzer.git](https://github.com/Pranshu475/smart-youtube-analyzer.git)
cd smart-youtube-analyzer

2. Backend Setup (Python)
cd ai_engine
# Install dependencies
pip install flask flask-cors google-api-python-client textblob scikit-learn transformers
# Start the Server
python app.py

3. Frontend Setup (React)
Open a new terminal:
cd client
# Install dependencies
npm install
# Start the React App
npm start

📜 Project Structure
/ai_engine: Python Flask Server & ML Models
/client: React Frontend Application


