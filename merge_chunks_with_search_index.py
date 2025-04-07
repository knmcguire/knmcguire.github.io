import json
import os

# Paths
search_index_path = "_site/search/search_index.json"  # Path to the existing search index
chunks_file = "blog_chunks.json"  # JSON file with the scraped chunks

def merge_chunks_with_search_index():
    """Merge chunks from blog_chunks.json into search_index.json and add them to the end."""
    if not os.path.exists(search_index_path):
        print(f"Error: {search_index_path} not found.")
        return

    if not os.path.exists(chunks_file):
        print(f"Error: {chunks_file} not found.")
        return

    # Load the existing search index
    with open(search_index_path, "r", encoding="utf-8") as f:
        search_index = json.load(f)

    # Load the chunks
    with open(chunks_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    # Mark external links in the title or text
    for chunk in chunks:
        if chunk["location"].startswith("http"):
            chunk["title"] = f"{chunk['title']} [External Link]"
            chunk["text"] = f"{chunk['text']} (This link opens an external website.)"

    # Append the chunks to the docs array
    search_index["docs"].extend(chunks)

    # Save the updated search index
    with open(search_index_path, "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)
    print(f"Appended {len(chunks)} chunks to {search_index_path}")

if __name__ == "__main__":
    merge_chunks_with_search_index()