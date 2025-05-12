from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.form['text']
    sentiment = get_sentiment(user_text)
    return render_template('index.html', text=user_text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
