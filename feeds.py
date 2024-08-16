import requests
import xml.etree.ElementTree as ET
from dateutil import parser
import re
from feeds_config import FEEDS

def extract_image_from_content(content):
    """Extract the first image URL from the content using regex."""
    match = re.search(r'<img[^>]+src="([^">]+)"', content)
    return match.group(1) if match else None

def fetch_articles():
    """
    Fetch articles from the feeds listed in FEEDS configuration.
    For each feed, parse the RSS feed and extract relevant article details.
    """
    articles = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for feed in FEEDS:
        response = requests.get(feed['url'])  # Fetch the RSS feed
        
        if response.status_code == 200:
            root = ET.fromstring(response.content)  # Parse XML content
            ns = feed.get('image_ns', {})  # Get namespaces for images
            content_ns = feed.get('content_ns', {})  # Get namespaces for content
            
            # List to temporarily store feed articles
            feed_articles = []
            
            # Iterate through each item (article) in the feed
            for item in root.findall(".//item"):
                title = item.find("title").text  # Extract article title
                link = item.find("link").text  # Extract article link
                pub_date = item.find("pubDate").text  # Extract publication date
                timestamp = parser.parse(pub_date)  # Parse date to a datetime object
                
                # Extract image URL from <enclosure> or other image tags if available
                image = item.find(feed.get('image_xpath', '.'), namespaces=ns)
                image_url = image.get("url") if image is not None else None
                
                # If no image found, attempt to extract it from content
                if not image_url and feed.get('content_xpath'):
                    content = item.find(feed['content_xpath'], namespaces=content_ns)
                    content_text = content.text if content is not None else ""
                    image_url = extract_image_from_content(content_text)
                
                # Append article details to feed_articles list
                feed_articles.append({
                    "title": title,
                    "link": link,
                    "timestamp": timestamp,
                    "source": feed['source'],
                    "image": image_url,
                    "source_url": feed['source_url']
                })
            
            # Remove duplicate if the first two items have the same title
            if len(feed_articles) > 1 and feed_articles[0]['title'] == feed_articles[1]['title']:
                feed_articles.pop(0)
            
            # Add the remaining articles to the main articles list
            articles.extend(feed_articles)
    
    return articles
