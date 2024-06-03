# PC-Crawler

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Initialize the Scrapy project:
    ```bash
    scrapy startproject pc_crawler
    ```

## Running the Scraper

```bash
scrapy crawl pc_spider
