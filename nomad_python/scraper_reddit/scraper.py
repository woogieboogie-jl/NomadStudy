import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def scraper(NFT_requested):
    print(NFT_requested)
    NFT_aggregated = {}
    news_list = []
    url = f"https://www.reddit.com/r/{NFT_requested}/top/?t=month"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r = requests.get(url, headers = headers)
    soup_news_list = bs(r.text,'html.parser').select('.rpBJOHq2PR60pnwJlUyP0 > div')
    for soup_news in soup_news_list[1:]:
        NFT_aggregated_news = {
            "title" : soup_news.select_one('div > div > a > div > h3').get_text(),
            "link" : soup_news.select_one('div > div > div > a')["href"],
            "upvote" : soup_news.select_one('.voteButton').next_sibling.get_text(),
            "thread" : NFT_requested 
        }
        news_list.append(NFT_aggregated_news)
    NFT_aggregated["time"] = datetime.now()
    NFT_aggregated["news_list"] = news_list
    return NFT_aggregated


    