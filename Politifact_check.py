from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Define search query
query = "climate change"
search_url = f"https://www.politifact.com/search/?q={query.replace(' ', '+')}"

# Open search URL
driver.get(search_url)

# Wait for elements to load
wait = WebDriverWait(driver, 10)

# Extract article titles and links
articles = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "m-teaser__title")))

# Extract metadata (author & date)
metadata = driver.find_elements(By.CLASS_NAME, "m-teaser__meta")

# Print results
if articles:
    for i in range(len(articles)):
        title_element = articles[i].find_element(By.TAG_NAME, "a")
        title = title_element.text.strip()
        link = "https://www.politifact.com" + title_element.get_attribute("href")

        meta_text = metadata[i].text.strip() if i < len(metadata) else "No metadata"

        print(f"\n📰 Title: {title}\n🔗 Link: {link}\n📅 Meta: {meta_text}")
else:
    print("No articles found.")

# Close driver
driver.quit()
