
import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
import time 
import schedule
import config
 

def save_to_csv(articles_data, filename=config.OUTPUT_FILE):
    file_exists = os.path.exists(filename)
    existing_links = set()
    if file_exists:
        with open(filename, "r", encoding = "utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_links.add(row['link'])
            
    with open(filename, "a", newline="", encoding = "utf-8" ) as f:
        fieldnames = ["title", "source", "date", "link", "keyword", "scraped_at"]
        writer = csv.DictWriter(f, fieldnames= fieldnames , quoting=csv.QUOTE_ALL)
        if not file_exists:
            writer.writeheader()

        new_count = 0
        for article in articles_data:
            if article['link'] not in existing_links:
                article["scraped_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow(article)
                new_count += 1

    print(f"saved {new_count} new articles to {filename}")

            


def scrape_news(keyword):
    formatted_keyword = keyword.replace(" ", "+") #user enters a string, replace spcaes with +, and store the result in formatted keyword variable

    url = f"https://news.google.com/rss/search?q={formatted_keyword}&hl={config.LANGUAGE}-{config.COUNTRY}&gl={config.COUNTRY}&ceid={config.COUNTRY}:{config.LANGUAGE}" #construct the URL for Google News RSS feed using the formatted keyword
    print(f"Fetching news for : {keyword}")
    print(f"URL : {url}")


    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful")
    else:
        print(f"Request failed : Status code {response.status_code}")
        return 


    soup = BeautifulSoup(response.content, "xml") 
    articles = soup.find_all('item')
    print(f"Found {len(articles)} articles")
    
    articles_data = []
    

    for article in articles:
        scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        title = article.find('title').text.strip()
        link = article.find('link').text.strip()
        pub_date = article.find('pubDate').text.strip()
        source = article.find('source').text.strip()
        # print("---")
        # print(f"Title: {title}")
        # print(f"Source: {source}")
        # print(f"Date: {pub_date}")
        # print(f"Link: {link}")
        
        articles_data.append({
            "title" : title,
            "source" : source,
            "date" : pub_date,
            "link" : link,
            "keyword" : keyword,
            "scraped_at" : scraped_at
        })

    save_to_csv(articles_data)

def run_all_keywords():
    print(f"Starting sracpe at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    for keyword in config.keywords:
        scrape_news(keyword)
        print("\n")
    print(f" ✅ Finished scraping at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

run_all_keywords()

schedule.every().day.at(config.SCHEDULE_TIME).do(run_all_keywords)

print("\n⏰ Scheduler is running... Press Ctrl+C to stop")

while True:
    schedule.run_pending()
    time.sleep(60)



