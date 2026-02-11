from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
from googleapiclient.discovery import build
import pickle

app = Flask(__name__)
CORS(app)

# --- PASTE YOUR API KEY HERE ---
API_KEY = ""

# 1. LOAD THE ML BRAIN (Spam/Question Classifier)
try:
    with open("model_v1.pkl", "rb") as f:
        vectorizer, classifier = pickle.load(f)
    print("✅ ML Classifier Loaded Successfully!")
except Exception as e:
    print(f"⚠️ Warning: ML Model not found. Did you run train_model.py? Error: {e}")
    vectorizer, classifier = None, None

# 2. LOAD THE NLP BRAIN (Summarizer)
summarizer = None
try:
    from transformers import pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    print("✅ AI Summarizer Loaded Successfully!")
except:
    print("⚠️ Heavy AI Engine not found. Running in Lite Mode.")

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    return url

@app.route('/analyze', methods=['POST'])
def analyze_comments():
    data = request.json
    video_url = data.get('url')
    
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    video_id = get_video_id(video_url)
    
    try:
        youtube = build("youtube", "v3", developerKey=API_KEY)
        request_yt = youtube.commentThreads().list(
            part="snippet", videoId=video_id, maxResults=50
        )
        response = request_yt.execute()
        
        comments_data = []
        all_text_for_summary = ""
        positive_count = 0
        negative_count = 0
        
        for item in response['items']:
            comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            all_text_for_summary += comment_text + ". "
            
            # --- A. SENTIMENT ANALYSIS ---
            analysis = TextBlob(comment_text)
            sentiment_score = analysis.sentiment.polarity
            
            if sentiment_score > 0:
                sentiment = "Positive"
                positive_count += 1
            elif sentiment_score < 0:
                sentiment = "Negative"
                negative_count += 1
            else:
                sentiment = "Neutral"

            # --- B. ML CLASSIFICATION (The New Part) ---
            category = "General"
            if classifier:
                # Turn text into numbers
                text_vector = vectorizer.transform([comment_text])
                # Ask the brain: "What is this?"
                category = classifier.predict(text_vector)[0]

            comments_data.append({
                "author": author,
                "text": comment_text,
                "sentiment": sentiment,
                "score": sentiment_score,
                "category": category  # <--- Sending this to React
            })
            
        # --- C. GENERATE SUMMARY ---
        if summarizer:
            try:
                summary_output = summarizer(all_text_for_summary[:2000], max_length=60, min_length=20, do_sample=False)
                summary_text = summary_output[0]['summary_text']
            except:
                summary_text = "Analysis complete."
        else:
            summary_text = f"Analyzed {len(comments_data)} comments. Mostly { 'Positive' if positive_count > negative_count else 'Negative' }."

        return jsonify({
            "total_comments": len(comments_data),
            "positive": positive_count,
            "negative": negative_count,
            "neutral": len(comments_data) - (positive_count + negative_count),
            "summary": summary_text,
            "comments": comments_data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)