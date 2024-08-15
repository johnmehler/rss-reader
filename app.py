from flask import Flask, render_template
from feeds import fetch_articles

app = Flask(__name__)

@app.route('/')
def index():
    """
    Home route that fetches articles and renders them in the index.html template.
    Articles are sorted by their timestamp, with the most recent first.
    """
    articles = fetch_articles()  # Fetch articles from the feeds
    
    # Sort articles by timestamp (most recent first)
    articles.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
