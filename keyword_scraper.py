import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
import re


def make_soup(url):
    # Fetching the content of the website
    response = requests.get(url)
    html_content = response.text
    # Parsing the content using BS
    soup = BeautifulSoup(html_content, "html.parser")
    # Extract the text from the html
    text = soup.get_text()
    new_text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    return new_text


def extract_keywords(website_text, min_length, max_length):
    # Init Rake object
    r = Rake(language="english",
             min_length=min_length,
             max_length=max_length,
             include_repeated_phrases=False)
    # Extract keywords from the text
    r.extract_keywords_from_text(website_text)
    # Get keywords with scores
    keywords_with_scores = r.get_ranked_phrases_with_scores()
    # Filter out phrases that have more than X number of words
    return keywords_with_scores


start_extraction = True
while start_extraction:

    # URL of website to parse
    url = input("URL of page to scrape: ")
    while True:
        if url.startswith("https://"):
            break
        else:
            print("Enter URL including https://")
            url = input("URL of page to scrape: ")
            continue

    # Controls how long the key phrases will be
    while True:
        try:
            min_length = int(input("Enter min length for key phrases: "))
            break
        except ValueError:
            print("Enter a number!")
    while True:
        try:
            max_length = int(input("Enter max length for key phrases: "))
            break
        except ValueError:
            print("Enter a number!")

    while min_length > max_length:
        print("min length is greater than max length")
        min_length = int(input("Enter min length for key phrases: "))
        max_length = int(input("Enter max length for key phrases: "))

    # Calls the BeautifulSoup funct
    website_text = make_soup(url)

    # Calls the rake funct
    key_phrases = extract_keywords(website_text, min_length, max_length)

    # Saves keywords & scores to a file
    for score, keyword in key_phrases:
        f = open("keywordlist.csv", "a")
        f.write(f"{score:.2f}:{keyword}")
        f.write("\n")
        f.close()

    # Continue or exit extraction
    carry_on = input("Scrape another URL? (Yes or No): ")
    while carry_on.lower() not in ("yes", "y", "no", "n"):
        print("Invalid input")
        carry_on = input("Scrape another URL? (Yes or No): ")
        if carry_on.lower() in ("yes", "y", "no", "n"):
            break
        if carry_on.lower() not in ("yes", "y", "no", "n"):
            continue
    if carry_on.lower() in ("yes", "y"):
        continue
    else:
        start_extraction = False
