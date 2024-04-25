import logging

from constants import SEARCH_QUERY, STATIC, LOGS_FILE
from scrapper import CollectFreshNews

# Configure logging
logging.basicConfig(
    filename=f"{STATIC}{LOGS_FILE}",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    filemode='w'
)

if __name__ == '__main__':
    fresh_news = CollectFreshNews(SEARCH_QUERY)
    fresh_news.task()
