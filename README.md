# Scraping and Analysis of the real estate market in Ivano-Frankivsk

## Features
- Web Scraping: Utilizes Scrapy to crawl and extract information from lun.ua.

- Data Analysis: Provides statistical analysis on the collected data.

- Machine Learning model: unfortunately i'm not experienced in ML, but i tried to do something. I hope you will not be too strict :)

## Installation

To clone this project from GitHub, follow these steps:

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where you want to clone the project.**
3. **Run the following commands:**
```shell
git clone https://github.com/ArturPoltser/py-scrape-and-analisys-of-real-estate-market.git
cd py-scrape-and-analisys-of-real-estate-market
python -m venv venv
venv\Scripts\activate  #for MacOS/Linux use: source venv/bin/activate
```

4. **Install requirements:**

```shell
pip install -r requirements.txt
```

5. **Run the Web Scraping Script:**

For analysis:
```shell
scrapy crawl real_estate_spider -O real_estate.csv
```
For machine learning:
```shell
scrapy crawl spider_for_ml -O real_estate_for_ML.json
```

## Files Structure

- `real_estate_scraper/spiders/real_estate_spider.py`: File that contains all main logic for scraping data for Statistical Analysis.
- `real_estate_scraper/spiders/spider_for_ml.py`: File that contains all main logic for scraping data for Machine Learning.
- `real_estate_analysis/analysis.ipynb`: Jupyter Notebook file containing the analysis of data.
- `machine_learning/ml_model.ipynb`: Jupyter Notebook file containing the machine learning model for price predictions.