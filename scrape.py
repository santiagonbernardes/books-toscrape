import logging
import re
import sys

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://books.toscrape.com/catalogue/page-{page_number}.html"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def build_book(book_element):
    title = book_element.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    price = book_element.find_element(By.CSS_SELECTOR, "p.price_color").text
    availability = book_element.find_element(
        By.CSS_SELECTOR, "p.instock.availability"
    ).text.strip()
    star_class = book_element.find_element(
        By.CSS_SELECTOR, "p[class*='star-rating']"
    ).get_attribute("class")
    rating_word = re.search(r"star-rating (\w+)", star_class).group(1)
    rating_numeric = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}.get(
        rating_word, 0
    )

    return {
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating_numeric,
    }


def scrape_books(driver, url):
    logger.info("Scraping url: %s", url)
    driver.get(url)
    total_count = 1000
    books = driver.find_elements(By.XPATH, "//article[@class='product_pod']")
    scraped_books = [build_book(book) for book in books]

    return scraped_books, total_count


def save_to_csv(books):
    df = pd.DataFrame(books)
    df.to_csv("books.csv", index=False)


if __name__ == "__main__":
    try:
        books, total_count = scrape_books(driver, BASE_URL.format(page_number=1))

        if not books or total_count == 0:
            logger.error("No books were found. Check the URL.")
            sys.exit(1)

        number_of_pages = total_count // len(books)

        # The first page was scraped in the step above, so we skip it
        for page_number in range(2, number_of_pages + 1):
            more_books, _ = scrape_books(
                driver, BASE_URL.format(page_number=page_number)
            )
            for book in more_books:
                books.append(book)

        save_to_csv(books)

        logger.info("Finished scraping.")
    finally:
        driver.quit()
