# Web Crawler with Multithreading & Multiprocessing

Web Crawler is a Python-based application that allows you to crawl and analyze web pages, extracting information such as page titles, meta descriptions, images, and links.

### Working Link: https://web-crawler-vyc1.onrender.com/

## Features

- Crawl multiple websites simultaneously using multithreading.
- Extract and display page titles, meta descriptions, images, and links.
- Utilize multiprocessing for efficient data extraction and analysis.
- Interactive web interface for easy usage.

## Multithreading

Multithreading is used in this web crawler to enable concurrent execution of multiple crawling tasks. Each website to be crawled is assigned to a separate thread, allowing multiple websites to be processed simultaneously. This improves the overall crawling speed and efficiency.

## Multiprocessing

Multiprocessing is employed for efficient data extraction and analysis. While crawling, the application utilizes multiple processes to extract information from web pages in parallel. This further enhances the performance and allows for faster data retrieval.

## Customization

You can customize the behavior and appearance of the web crawler by modifying the Python code and CSS styles in the project files. For example, you can change the background image or add more features to the crawler.

## Deployment

To deploy this application in a production environment, you can use web server software like Gunicorn or deploy it to a cloud platform like Render. Ensure that you follow the deployment best practices for your chosen hosting environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The web framework used.
- [requests](https://docs.python-requests.org/en/latest/) - HTTP library for making requests.
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library for web scraping.
