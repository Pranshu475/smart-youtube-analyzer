import requests

# 1. The URL of your local server
url = "http://127.0.0.1:5000/analyze"

# 2. The data we are sending (Simulating a user pasting a link)
payload = {
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll video again
}

# 3. Send the POST request
print("Sending request to server...")
try:
    response = requests.post(url, json=payload)
    
    # 4. Print the answer from the 'Brain'
    print("\n--- SERVER RESPONSE ---")
    print(response.json())
    
except Exception as e:
    print(f"Error: {e}")
    print("Make sure your other terminal is still running 'python app.py'!")