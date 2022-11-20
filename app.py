from flask import Flask, jsonify
import requests
from utils import extracted_summary
from json import dumps
app = Flask(__name__)

@app.route('/')
def index():
    news_articles = requests.get('https://newsdata.io/api/1/news?apikey=pub_13631d1dbb14985f818a6e650715436915fa5&q=politics&language=en').json()['results']
    news_articles = [a for a in news_articles if a["image_url"]]
    article = news_articles[0]
    summary = extracted_summary(article['description'], length=1) if article['description'] else extracted_summary(article['content'], length=1)

    news = {
        "headline": article["title"],
        "summary": summary,
        # "sentiment": sentiment(summary),
        "image_url": article["image_url"]
    }

    response = jsonify(news)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/greet')
def say_hello():
    return 'Hello from Server'