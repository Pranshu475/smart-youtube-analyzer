import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Expanded Dataset (Now with 'General' category!)
data = [
    # --- APPRECIATION (Positive Feedback) ---
    ("Great video thanks", "Appreciation"),
    ("Love this content", "Appreciation"),
    ("Very helpful tutorial", "Appreciation"),
    ("Amazing work keep it up", "Appreciation"),
    ("Best explanation ever", "Appreciation"),
    ("Thanks for sharing", "Appreciation"),
    ("Good job", "Appreciation"),
    ("Wow this is awesome", "Appreciation"),
    ("I learned a lot", "Appreciation"),
    ("This saved my life", "Appreciation"),

    # --- QUESTIONS (Looking for help) ---
    ("How do I fix this error?", "Question"),
    ("Can you share the code?", "Question"),
    ("Where is the link?", "Question"),
    ("Does this work on Mac?", "Question"),
    ("What theme are you using?", "Question"),
    ("Is this python or java?", "Question"),
    ("Help me please", "Question"),
    ("Why is my code crashing?", "Question"),
    ("When will you upload part 2?", "Question"),
    ("Any solution for this bug?", "Question"),
    ("?", "Question"),  # Single question mark

    # --- SPAM (Self-promo / Scams) ---
    ("Subscribe to my channel", "Spam"),
    ("Check out my video", "Spam"),
    ("Click this link for free money", "Spam"),
    ("Follow me back", "Spam"),
    ("Visit my website", "Spam"),
    ("Free gift card here", "Spam"),
    ("sub4sub", "Spam"),
    ("invest in crypto now", "Spam"),
    ("dating girls link", "Spam"),
    ("whatsapp number", "Spam"),

    # --- GENERAL (Random chatter / Opinions / Politics) ---
    ("This is boring", "General"),
    ("I disagree with this", "General"),
    ("The audio is too low", "General"),
    ("First comment", "General"),
    ("I am watching this in 2026", "General"),
    ("He is wrong about the politics", "General"),
    ("Liberals are complaining", "General"),  # Specific fix for your screenshot
    ("Government needs to change", "General"),
    ("That looks crazy", "General"),
    ("Not sure about this", "General"),
    ("Just passing by", "General"),
    ("lol", "General"),
    ("weird video", "General"),
    ("Okay", "General")
]

# Separate text and labels
texts = [text for text, label in data]
labels = [label for text, label in data]

# Vectorization
print("🧮 Converting text to numbers...")
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Training
print("🧠 Training the Brain (Smarter Version)...")
classifier = MultinomialNB()
classifier.fit(X, labels)

# Saving
print("💾 Saving the model...")
with open("model_v1.pkl", "wb") as f:
    pickle.dump((vectorizer, classifier), f)

print("✅ DONE! New smarter model created.")