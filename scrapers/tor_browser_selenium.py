# scrapers/tor_browser_selenium.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from utils.leak_detector import detect_leaks
from database.db import store_leak
from datetime import datetime
import os
import time

def browse_onion_site(url):
    options = Options()
    options.headless = True
    options.set_preference("network.proxy.type", 1)
    options.set_preference("network.proxy.socks", "127.0.0.1")
    options.set_preference("network.proxy.socks_port", 9050)
    options.set_preference("network.proxy.socks_remote_dns", True)

    service = Service()  # uses geckodriver from PATH
    driver = webdriver.Firefox(service=service, options=options)

    try:
        print(f"🌐 Visiting: {url}")
        driver.get(url)
        time.sleep(10)

        body = driver.find_element(By.TAG_NAME, "body").text
        leak_types = detect_leaks(body)

        if leak_types:
            print(f"🧨 Leak Detected: {leak_types}")
            store_leak(url, ", ".join(leak_types), body[:300])
        else:
            print("✅ No leaks found")

        # Screenshot
        os.makedirs("screenshots", exist_ok=True)
        safe_name = url.replace("http://", "").replace("/", "_")[:60]
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{safe_name}_{timestamp}.png"
        driver.save_screenshot(path)
        print(f"📸 Screenshot saved: {path}")

    except Exception as e:
        print(f"❌ Error crawling {url}: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    with open("onion_sites.txt") as f:
        sites = [line.strip() for line in f if line.strip()]
    for site in sites:
        browse_onion_site(site)
