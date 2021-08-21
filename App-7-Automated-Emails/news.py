import requests
from datetime import datetime, timedelta


class NewsFeed:
    """
    Representing multiple news titles and links as a single string.
    Get the API Key from https://newsapi.org
    """
    base_url = "https://newsapi.org/v2/everything?"
    apiKey = "<Your Api Key>"
    date = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")

    def __init__(self, interest, language, from_date=date):
        self.interest = interest
        self.from_date = from_date
        self.language = language

    def get(self):
        url = f"{self.base_url}qInTitle={self.interest}&from={self.from_date}" \
              f"&sortBy=publishedAt&language={self.language}&apiKey={self.apiKey} "
        response = requests.get(url)
        content = response.json()

        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body
