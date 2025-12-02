import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Optional test
test_sentence = "I love this banking app, it's really useful!"
print(sid.polarity_scores(test_sentence))
