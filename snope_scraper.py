from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

def extract_title_from_url(url):
    """Extracts a readable title from a Snopes URL if the title is missing."""
    if not url:
        return None  # Return None so we can filter it out later
    
    match = re.search(r'/([^/]+)/?$', url.rstrip('/'))
    if match:
        raw_title = match.group(1).replace("-", " ").title()
    else:
        raw_title = None  # Return None if extraction fails

    return raw_title

def scrape_snopes(query):
    """Scrapes Snopes search results for a given query."""
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    search_url = f"https://www.snopes.com/?s={query.replace(' ', '+')}"
    driver.get(search_url)

    time.sleep(5)  # Allow time for JavaScript to load results

    search_results = driver.find_elements(By.CSS_SELECTOR, "div.gs-webResult")

    if not search_results:
        print("❌ No search results found. Page structure might have changed.")
        driver.quit()
        return []

    results = []
    for result in search_results:
        try:
            title_element = result.find_element(By.CSS_SELECTOR, "a.gs-title")
            title = title_element.text.strip()
            link = title_element.get_attribute("href")

            # If title is empty, extract from URL
            if not title:
                title = extract_title_from_url(link)

            # Only add if valid title and URL exist
            if title and link:
                results.append({"title": title, "url": link})
        except Exception as e:
            print("Skipping an article due to error:", e)

    driver.quit()
    return results

# 🔍 Test the scraper
fact_checks = scrape_snopes("climate change")
for f in fact_checks:
    print(f)
