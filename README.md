# 🛒 eBay Data Scraper (UI-Based)

This project is a **UI-based Python web scraper** for extracting eBay product data using `requests` and `BeautifulSoup`.  
It is designed to run with a simple graphical interface (`scrap.ui`) and demonstrates reading multiple URLs and pages automatically.

---

## 📌 About the Project

This scraper collects:
- Product names
- Conditions
- Prices
- Original prices
- Discounts
- Sold quantities
- Shipping costs
- Seller locations

Data is stored in a **CSV file (`eBayData.csv`)** for easy analysis.

---

## 🧩 How It Works

1. **Read URLs:**  
   Loads a list of eBay category/search URLs from `urlFile.txt`.

2. **Track Progress:**  
   Uses `data.txt` to save the current URL index and page number. This helps resume scraping from where you left off.

3. **Scrape Pages:**  
   Iterates through pages (up to 70) for each URL, collects all product details, and appends them to lists.

4. **Save Data:**  
   Combines all scraped data into a Pandas DataFrame and saves it as `eBayData.csv`.

---

## ⚙️ Technologies Used

- **Language:** Python
- **Libraries:** `requests`, `BeautifulSoup`, `pandas`
- **UI:** Built with `scrap.ui`

---

## 📁 Project Structure

```
YourProject/
├── scrap.ui           # UI file for the scraper (PyQt/Designer)
├── part2.py            # Python script for scraping logic
├── urlFile.txt        # Text file containing all base URLs to scrape
├── data.txt           # Tracks the current URL index and page number
├── eBayData.csv       # Final output data file
└── README.md          # Project documentation
```

---

## ✅ Key Features

- 📄 Reads multiple URLs from a file
- 🔄 Automatically navigates multiple pages
- 💾 Saves data as CSV for easy analysis
- 🔎 Uses BeautifulSoup for HTML parsing
- 🔗 Tracks scraping progress for long runs

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/3rdSem_Scrapping-eBayData.git
   cd 3rdSem_Scrapping-eBayData
   ```

2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

3. **Run the script:**
   ```bash
   python part2.py
   ```

4. **Check your CSV file:**
   The scraped data will be saved as `eBayData.csv` in the project folder.

---

## 👤 Author

**Iqra Tariq**  
_Developed as a 3rd Semester Python Data Scraping Project._

---

## 📜 License

This project is for academic and learning purposes.  
Feel free to fork, improve, and adapt it for your own scraping needs — responsibly!

