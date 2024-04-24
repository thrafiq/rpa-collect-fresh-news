import logging

from constants import AMOUNT_INDICATORS

XPATH_CONFIG = {
    'search_button': '//div[@class="site-header__search-trigger"]//button[@class="no-styles-button"]',
    'search_input': '//input[@class="search-bar__input"]',
    'submit_search': '//div[@class="search-bar__button"]//button[@type="submit"]',
    'search_result_list': '//div[@class="search-result__list"]',
    'no_result_indication': '//div[@class="search-results__no-results"]',
    'sorter': '//select[@id="search-sort-option"]',
    'show_more': '//button[@class="show-more-button grid-full-width"]',
    'loading_show_more': '//div[@class="loading-animation"]',
    'title': './/h3[@class="gc__title"]//span',
    'date': './/footer[@class="gc__footer"]//span[@class="screen-reader-text"]',
    'description': './/div[@class="gc__excerpt"]//p',
    'filename': './/div[@class="responsive-image"]//img',
    'article': '//div[@class="search-result__list"]//article[@class="gc u-clickable-card gc--type-customsearch#result '
               'gc--list gc--with-image"]'
}


def is_amount_mentioned(string):
    """Checks if any amount is mentioned in the string"""
    try:
        string_in_lower = string.lower()
        for indicator in AMOUNT_INDICATORS:
            if indicator in string_in_lower:
                return True
        return False
    except Exception as e:
        logging.error(f"Error checking if amount mentioned: {e}")
        return False
