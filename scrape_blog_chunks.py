import requests
from bs4 import BeautifulSoup
import json
import yaml
import os

# Paths
urls_file = "urls.yaml"  # YAML file containing the list of URLs
output_chunks_file = "blog_chunks.json"  # JSON file to store the chunks

def split_text_into_chunks(text, chunk_size=200):
    """Split text into chunks of approximately `chunk_size` words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def load_urls_from_yaml():
    """Load URLs from a YAML file."""
    if not os.path.exists(urls_file):
        print(f"Error: {urls_file} not found.")
        return []

    with open(urls_file, "r", encoding="utf-8") as f:
        urls = yaml.safe_load(f)
        return [entry.get("url") for entry in urls if "url" in entry]

def scrape_blog_posts(urls):
    """Scrape blog posts and split their content into chunks."""
    chunks = []

    for url in urls:
        print(f"Scraping: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract the title
            title_tag = soup.find("title")
            title = title_tag.get_text(strip=True) if title_tag else "No Title"

            # Extract the main content (adjust the selector based on the site's structure)
            content_div = soup.find("div", class_="entry-content")
            if not content_div:
                print(f"Warning: No content found for {url}")
                continue

            # Extract all paragraphs from the content
            text = " ".join(p.get_text(strip=True) for p in content_div.find_all("p"))

            # Split the content into chunks
            text_chunks = split_text_into_chunks(text, chunk_size=200)
            for i, chunk in enumerate(text_chunks):
                chunks.append({
                    "location": f"{url}#chunk-{i+1}",
                    "title": f"{title} (Part {i+1})",
                    "text": chunk.strip()
                })

        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")

    return chunks

def save_chunks_to_json(chunks):
    """Save the chunks to a JSON file."""
    with open(output_chunks_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(chunks)} chunks to {output_chunks_file}")

if __name__ == "__main__":
    # Step 1: Load URLs from the YAML file
    blog_post_urls = load_urls_from_yaml()

    if not blog_post_urls:
        print("No URLs found in the YAML file. Exiting.")
    else:
        # Step 2: Scrape blog posts and split them into chunks
        blog_post_chunks = scrape_blog_posts(blog_post_urls)

        # Step 3: Save the chunks to a JSON file
        save_chunks_to_json(blog_post_chunks)