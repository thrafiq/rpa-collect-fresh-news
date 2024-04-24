import logging

from constants import SEARCH_QUERY
from scrapper import CollectFreshNews

# Configure logging
logging.basicConfig(
    filename='collect_fresh_news.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)

if __name__ == '__main__':
    fresh_news = CollectFreshNews(SEARCH_QUERY)
    fresh_news.task()
