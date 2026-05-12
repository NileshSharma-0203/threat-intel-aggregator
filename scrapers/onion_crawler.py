import requests
from bs4 import BeautifulSoup
from database.db import store_leak
import schedule
import time
import re

# Proxy through Tor
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Keywords for quick scanning
keywords = [
    'aadhaar', 'pan card', 'passport', 'voter id', 'indian bank',
    'upi', 'ifsc', 'gov.in', 'nic.in', 'aadhar', 'kyc', 'phonepe',
    'paytm', 'income tax', 'cybercrime', 'credit card dump', 'account number'
]

# Regex for structured leak patterns
regex_patterns = {
    "aadhaar": r"\b\d{4}\s\d{4}\s\d{4}\b",
    "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "passport": r"\b[A-Z]{1}-?[0-9]{7}\b",
    "ifsc": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
    "bank_ac": r"\b\d{9,18}\b"
}

def crawl_site(url):
    try:
        response = requests.get(url, proxies=proxies, timeout=20)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"✅ Crawled: {url}")
            print("   Title:", soup.title.string.strip() if soup.title else "No Title")

            page_text = soup.get_text().lower()

            # Keyword match
            for keyword in keywords:
                if keyword in page_text:
                    index = page_text.find(keyword)
                    snippet = page_text[index-50:index+50].replace('\n', ' ')
                    print(f"   🔍 Found keyword: {keyword}")
                    store_leak(url, keyword, snippet)

            # Regex pattern match
            for label, pattern in regex_patterns.items():
                matches = re.findall(pattern, page_text)
                for match in matches:
                    print(f"   🧬 Regex match: {label} → {match}")
                    store_leak(url, label, match)

        else:
            print(f"❌ Failed: {url} (Status {response.status_code})")
    except Exception as e:
        print(f"⚠️ Error crawling {url}: {e}")

def crawl_all():
    print("⏳ Starting crawl batch...")
    try:
        with open("scrapers/onion_sites.txt", "r") as f:
            sites = [line.strip() for line in f if line.strip()]
        for site in sites:
            crawl_site(site)
    except FileNotFoundError:
        print("❌ File not found: scrapers/onion_sites.txt")

if __name__ == "__main__":
    crawl_all()
    schedule.every(30).minutes.do(crawl_all)
    print("🕒 Crawler scheduled to run every 30 minutes.")
    while True:
        schedule.run_pending()
        time.sleep(1)
