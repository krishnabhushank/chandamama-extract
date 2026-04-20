import requests
import os
import time


def save_file(url, filename):
    """
    Downloads a file from a URL and saves it locally.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Successfully downloaded: {filename}")
            return True
        else:
            # Silently skip missing files if necessary
            print(f"Skipping {url} (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
        return False


def generate_urls():
    # Configuration based on your updated format
    start_year = 2006
    end_year = 2006
    base_url = "http://chandamama.in/resources"
    language = "english"  # Updated from 'telugu'
    file_count = 1

    if not os.path.exists("chandamama_english"):
        os.makedirs("chandamama_english")

    for current_year in range(start_year, end_year + 1):
        for current_month in range(1, 13):
            # Use zfill(2) to ensure month is '01' instead of '1'
            month_str = str(current_month).zfill(2)

            # Constructing the URL: .../english/2007/Chandamama-2007-01.pdf
            file_url = f"{base_url}/{language}/{current_year}/Chandamama-{current_year}-{month_str}.pdf"
            filename = f"chandamama_english/{file_count}-Chandamama-{current_year}-{month_str}.pdf"

            print(f"Requesting: {file_url}")
            if save_file(file_url, filename):
                file_count += 1

            # 0.2s delay to avoid overwhelming the server
            time.sleep(0.2)


if __name__ == "__main__":
    generate_urls()