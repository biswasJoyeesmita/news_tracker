# News Tracker — Automated Google News Scraper

A Python automation tool that tracks breaking news across multiple 
topics simultaneously, stores articles in a structured CSV database, 
and runs on a daily schedule — completely hands-free.

Built this because manually checking news sites for multiple topics 
every day is a waste of time. This does it for you.

---

## What It Does

- Pulls live news from Google News RSS for any keyword you define
- Tracks multiple topics in a single run
- Stores articles in a clean, structured CSV — title, source, 
  date, link, keyword, and timestamp
- Skips articles it has already saved — no duplicate entries, ever
- Timestamps each article at the exact moment it's saved
- Runs automatically every day at a time you set
- Fully configurable — change keywords and schedule without 
  touching the main code

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `requests` | Fetches Google News RSS feed |
| `BeautifulSoup4` | Parses XML response |
| `lxml` | XML parser engine |
| `schedule` | Runs the scraper daily |
| `csv` | Stores and reads article data |
| `datetime` | Timestamps every saved article |

---

## Project Structure
---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/news-tracker.git
cd news-tracker
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your keywords
Open `config.py` and set your topics:

```python
keywords = [
    "Artificial Intelligence",
    "Machine Learning",
    "climate change",
    "cryptocurrency",
    "virtual reality"
]

SCHEDULE_TIME = "09:00"  # 24hr format
```

### 5. Run
```bash
python scraper.py
```

The scraper runs immediately on start, then automatically 
every day at your scheduled time. Press `Ctrl+C` to stop.

---

## 📊 Sample Data

> Each article also includes a direct link to the original source.

| title | source | date | keyword | scraped_at |
|---|---|---|---|---|
| White House Considers Vetting A.I. Models Before They Are Released |The New York Times | Mon, 04 May 2026 22:37:30 GMT | Artificial Intelligence | 2026-05-05 22:08:13 |

| Edinburgh AI firm develops machine learning tool to accelerate woodland monitoring | Inside Ecology | Mon, 04 May 2026 22:37:30 GMT | Machine Learning | 2026-05-05 22:08:13 |

| Virtual Reality - Meaning, Types, Applications, Benefits | Vajiram & Ravi | Wed, 07 Jan 2026 08:00:00 GMT | virtual reality | 2026-05-07 22:27:52 |

---

## 🔍 How It Works

1. Reads keywords from `config.py`
2. Builds a Google News RSS URL for each keyword
3. Parses the XML response with BeautifulSoup
4. Compares each article link against existing saved links
5. Saves only new articles with a fresh timestamp
6. Repeats for every keyword
7. Sleeps until next scheduled run

---

## 📝 Notes

- Google News RSS returns approximately 100 articles per keyword
- Article links are Google News redirect URLs that forward 
  to the original source
- The duplicate check compares article links — so even if 
  a headline changes slightly, the same article won't be saved twice
- Changing keywords in `config.py` takes effect on the next run
  without touching `scraper.py`

---

## 🔮 Planned Improvements

- [ ] Sentiment analysis on headlines using TextBlob
- [ ] Daily email digest of new articles
- [ ] Web dashboard to visualize trends across keywords
- [ ] Export to Google Sheets
- [ ] Slack/Telegram notification for breaking news

---

## 👩‍💻 Author

**Joyeesmita Biswas**  
[GitHub](https://github.com/biswasJoyeesmita) • 
[LinkedIn](https://linkedin.com/in/YOUR_PROFILE)