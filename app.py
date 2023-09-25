# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

app = Flask(__name__)

# Define a function to crawl a URL and extract various information
def crawl_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract page title
            page_title = soup.title.string if soup.title else 'N/A'
            
            # Extract meta description
            meta_description = ''
            meta_tag = soup.find('meta', attrs={'name': 'description'})
            if meta_tag:
                meta_description = meta_tag.get('content')
            
            # Extract images
            images = [img.get('src') for img in soup.find_all('img')]
            
            # Extract all links
            links = [a.get('href') for a in soup.find_all('a')]
            
            return {
                'URL': url,
                'Title': page_title,
                'Meta Description': meta_description,
                'Images': images,
                'Links': links
            }
    except Exception as e:
        return {
            'URL': url,
            'Error': str(e)
        }

# Create a route for the web crawler frontend
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urls = request.form.get('urls')
        url_list = urls.split('\n')
        # Filter out empty lines and whitespace
        url_list = [url.strip() for url in url_list if url.strip()]
        
        # Multithreading for handling multiple URLs concurrently
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(crawl_url, url_list))
        
        return render_template('index.html', results=results)
    
    return render_template('index.html', results=[])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
