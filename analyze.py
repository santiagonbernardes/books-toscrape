import logging

import pandas as pd

INPUT_FILE = "books.csv"
OUTPUT_FILE = "books_analyzed.csv"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_and_clean_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)
        logger.info("Successfully loaded and cleaned data from %s", file_path)
        return df
    except FileNotFoundError:
        logger.error("Error: The file %s was not found.", file_path)
        return None
    except Exception as e:
        logger.error("An error occurred during data loading or cleaning: %s", str(e))
        return None


def classify_books_by_value(df):
    median_price = df["price"].median()
    logger.info("Calculated median price: £%s", f"{median_price:.2f}")
    df["value_category"] = df["price"].apply(
        lambda price: "High Value" if price > median_price else "Low Value"
    )
    logger.info("Successfully classified books by value.")
    return df


def save_analyzed_data(df, file_path):
    df.to_csv(file_path, index=False)
    logger.info("Analyzed data saved to %s", file_path)


if __name__ == "__main__":
    logger.info("Starting analysis of %s...", INPUT_FILE)
    book_df = load_and_clean_data(INPUT_FILE)

    if book_df is not None:
        analyzed_df = classify_books_by_value(book_df)
        save_analyzed_data(analyzed_df, OUTPUT_FILE)
        logger.info("Analysis finished.")
