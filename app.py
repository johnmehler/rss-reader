import logging
from flask import Flask, render_template
from feeds import fetch_articles

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def index():
    logging.info("Fetching articles for homepage")
    
    # Fetch articles from the feeds, sort them by newest
    articles = fetch_articles()  
    articles.sort(key=lambda x: x["timestamp"], reverse=True)
    
    logging.info(f"Fetched and sorted {len(articles)} articles")
    
    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(debug=True)
