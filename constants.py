import os

from RPA.Robocorp.WorkItems import WorkItems

SITE_URL = "https://www.aljazeera.com/"

SEARCH_QUERY = "Intense rainfall sweeps across Dubai and the wider United Arab Emirates"
SORT_BY = 'date'

DEBUG = os.getenv('DEBUG', default=True)

AMOUNT_INDICATORS = ["$", "dollars", "dollar", "USD", "usd"]

JS_SCRIPT = "window.scrollTo(0, document.body.scrollHeight)"

STATIC = './output/'
FILES_DIRECTORY = 'images'
ZIP_FILE = 'zip_images'
LOGS_FILE = 'collect_fresh_news.log'

if not DEBUG:
    work_items = WorkItems()
    work_items.get_input_work_item()
    payload = work_items.get_work_item_payload()
    SEARCH_QUERY = payload.get('search_query')
