import requests

# Replace with your NewsAPI key
NEWS_API_KEY = "1e9bbbc383874b31b5a070857dd05b3d"

def fetch_news(query, num_articles=5):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])[:num_articles]  # Get top 'num_articles'
        
        news_results = []
        for article in articles:
            news_results.append({
                "title": article["title"],
                "source": article["source"]["name"],
                "url": article["url"],
                "published_at": article["publishedAt"]
            })
        
        return news_results
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
news = fetch_news("climate change")
for n in news:
    print(n)
