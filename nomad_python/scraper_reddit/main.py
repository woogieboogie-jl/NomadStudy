import requests
from flask import Flask, render_template, request
from datetime import datetime
from scraper import scraper


DB = {}
NFTs_list = [
    "upfiring", 
    "lukso",  
    "minaprotocol"
    ]


def db_writer(DB,NFTs_requested):
    NFTs_aggregated = []
    for NFT_requested in NFTs_requested:
        if NFT_requested in DB and (datetime.now() - DB[NFT_requested]["time"]).seconds < 60:
            NFTs_aggregated += DB[NFT_requested]["news_list"]
        else:
            NFT_scraped = scraper(NFT_requested)
            DB[NFT_requested] = NFT_scraped
            NFTs_aggregated += NFT_scraped["news_list"]
    return NFTs_aggregated


app = Flask("NFT_CHECKER")

@app.route('/')
def home():
    return render_template("home.html", NFTs_list = NFTs_list)

@app.route('/aggregated')
def aggregated():
    # NFTs_requested = request.form.getlist("NFTs_requested")
    NFTs_requested = []
    for NFT in NFTs_list:
        if NFT in request.args:
            NFTs_requested.append(NFT)
    NFTs_aggregated = db_writer(DB,NFTs_requested)
    return render_template("aggregated.html", NFTs_aggregated = NFTs_aggregated, NFTs_requested = NFTs_requested)
        

app.run(host="0.0.0.0")


