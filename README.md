# Al Jazeera News Scraper

This is a robot for scraping fresh news from Al Jazeera (https://www.aljazeera.com/).

## Usage

1. Install requirements:
    Install basic requirements (run the following command)

        pip install -r requirements.txt

2. Run the scraper:

    If no search query is provided, the scraper will use the default query: "Intense rainfall sweeps across Dubai and the wider United Arab Emirates"


3. Output:

- The scraper will generate an `output` folder containing:
  - An `images` folder with all the images scraped from the Al Jazeera news page.
  - An `exported_data` Excel file (`exported_data.xlsx`) with the following columns:
    - Title
    - Date
    - Description
    - Image
    - Count phrase
    - Includes Amount
  - A `logs` file (`collect_fresh_news.log`).
  - The images will be zipped into a `zip_images.zip` file to minimize the `output` folder size.
Each run will replace the existing content in the output folder.
