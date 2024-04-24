from constants import SEARCH_QUERY
from scrapper import CollectFreshNews

if __name__ == '__main__':
    fresh_news = CollectFreshNews(SEARCH_QUERY)
    fresh_news.task()
