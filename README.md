# Keyword Scraper
Simple rapid automatic keyword extraction (RAKE) tool to scrape keywords from a URL. I built this to use for SEO research, to quickly pull lists of competitor keywords and to find new ideas for content creation. Could easily be modified to use for social media monitoring, customer service or sentiment analysis of customer reviews/feedback.
## Table of contents ##
[1. How to use](https://github.com/stuartmcq84/keywordscraper/edit/main/README.md#hot-to-use)
[2. Future developements](https://github.com/stuartmcq84/keywordscraper/edit/main/README.md#future-developments)
[3. Bugs](https://github.com/stuartmcq84/keywordscraper/edit/main/README.md#bugs)

## Hot to use ##
The following libraries need to be installed:<br>
* import requests
* from bs4 import BeautifulSoup
* from rake_nltk import Rake
* import re

Code can be run straight in your IDE or terminal. You'll be asked to enter the URL you want to scrape keywords from.<br>
Has to be the full domain (e.g. https://example.com).<br>
<br>
The next inputs will ask you to enter the min and max length for key phrases.<br>
Having experimented, a min length of 2 and max length of 4 seems to produce a decent set of keywords to start with.<br>
The keywords will be saved to keywordlist.csv. Each time you scrape a URL the new keywords are appended to the end.

## Future developments ##
1. Add option to compare keywords to Google Trends using PyTrends. Should make the data more useful as you'll be able to focus content creation on the most relevant keyword.
2. Add option to loop back and crawl the same URL again. This would be useful if you want short tail and long tail keywords from the same page but with different scores for each set. (you can do this now but have to enter the URL again).
3. Make code more efficient. This was the first attempt, pretty sure the code can be made more efficient.
4. Maybe an option to scrape multiple URLs. Currently it scrapes one at a time.

## Bugs ##
The Rake object constructor parameters includes include_repeated_phrases=False. However, this doesn't always work. Currently not sure why repated phrases are being included in the keywordlist.csv file.
