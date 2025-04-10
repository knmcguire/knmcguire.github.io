import os
import yaml
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re
from datetime import datetime

# Load URLs from urls.yaml
def load_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Scrape blog post content
def scrape_blog_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the main content (adjust the selector based on the website's structure)
        article = soup.find('article')  # Assuming blog content is inside <article>
        if article:
            # Remove images and links
            for img in article.find_all('img'):
                img.decompose()
            for link in article.find_all('a'):
                link.unwrap()
            return md(str(article))  # Convert HTML to Markdown
    return None

# Extract date from URL or use a default
def extract_date_from_url(url):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)  # Match YYYY/MM/DD in the URL
    if match:
        return match.group(1) + match.group(2) + match.group(3)  # Return YYYYMMDD
    match = re.search(r'/(\d{4})/(\d{2})/', url)  # Match YYYY/MM in the URL
    if match:
        return match.group(1) + match.group(2) + "01"  # Default to the first day of the month
    return datetime.now().strftime("%Y%m%d")  # Default to today's date

# Save content to a Markdown file
def save_to_markdown(content, file_name, output_dir, original_url):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, file_name)
    placeholder = f"**This is a placeholder for the original blogpost to be found here: [{original_url}](original_url)**\n\n"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(placeholder + content)

def main():
    urls_file = 'urls.yaml'
    output_dir = 'docs/blog/old_bitcraze_blogposts'

    # Load URLs
    urls = load_urls(urls_file)

    for entry in urls:
        url = entry['url'].strip()
        print(f"Scraping: {url}")
        content = scrape_blog_content(url)
        if content:
            # Extract date and generate a filename
            date_prefix = extract_date_from_url(url)
            file_name = f"{date_prefix}_{url.split('/')[-2]}.md"
            save_to_markdown(content, file_name, output_dir, url)
            print(f"Saved: {file_name}")
        else:
            print(f"Failed to scrape: {url}")

if __name__ == '__main__':
    main()