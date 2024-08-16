from flask import Flask, render_template
from feeds import fetch_articles

app = Flask(__name__)

@app.route('/')
def index():
    
    # Fetch articles from the feeds, sort them by newest
    articles = fetch_articles()  
    articles.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
