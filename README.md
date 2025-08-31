# Books - ToScrape

Checkpoint 4 deliverable.

## Team members

- [Cristiano Washington Dias](https://github.com/criswd) - RM555992
- [José Enrico dos Santos Tavares](https://github.com/joseenricotavares) - RM554471
- [Lucas Hidetoshi Ichiama](https://github.com/ichiamalucas) - RM555077
- [Marcia Ricardo Rosano](https://github.com/mrr2024) - RM557464
- [Mizael Vieira Bezerra](https://github.com/mizaelvieira1) - RM555796
- [Santiago Bernardes](https://github.com/santiagonbernardes) - RM557447

## Installation
1. **Clone the repository:**
   ```bash
   git clone git@github.com:santiagonbernardes/books-toscrape.git
   cd books-toscrape
   ```

2. **Install UV (package manager):**
   Instructions can be found [here](https://docs.astral.sh/uv/getting-started/installation/).

3. **Install dependencies:**
   ```bash
   uv sync

4. Run the scraper
```bash
  # this command you generate the books.csv file
  uv run scrape.py
```

5. Run the analyzer
```bash
  # this command will generate the books_analyzed.csv file
  uv run analyze.py
```
