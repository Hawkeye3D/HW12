# import necessary libraries
import pandas as pd
from flask import Flask, render_template
# %%
# Module used to connect Python with MongoDb
from flask_pymongo import PyMongo
import datetime
import pprint as pp
import pymongo
# Import Scrape libraries
import requests
import urllib.request
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


def SetupMarsDB():

    '''this is used to set and initialize the MongoDB
    It is used to create the DB if it is not already set up
    and then create a table referred to as 'collection and  then
    '''

    # The default port used by MongoDB is 27017
    # https://docs.mongodb.com/manual/reference/default-mongodb-port
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    # declare database
    db = client.mars_db  # implicitly declared mars DB
    collection = db.mars_db
    collection.drop()  # clean it out before we add the test data
  
   
    post = {'nasatitle': 'CORGIES ROAMING MARS!!',
            'nasanote': 'In a surprise development today  a pack of what appear to be cute Corgies were seen roaming an Ancient Alien ruin on Mars. This has completely rattled the scientfic community. Nay sayers claim it is just another example of fake news, but Corgie lovers world-wide say it is proof that Corgies are the best and brightest dog breed.',
            'nasaimgURL': 'https://media1.giphy.com/media/vGo2sgzeC8r60/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp',
            'nasacardimage': '',
            'nasadate': datetime.datetime.utcnow(),
            'jpl_featured_image_url': 'https://media1.giphy.com/media/wOJhrjx3lFxh9ShCZY/giphy.webp?cid=790b761122897cf1a00f010852e522814f44989b84eb167c&rid=giphy.webp',
            'mars_weather': 'Partly dusty, 70 degrees F, Raining Mainly Corgis in the Plains',
            'popups': ['1','2','3','4'],
            'hemispherepics': [{'Title': 'Water on Mars', 'hemisphere_url': 'https://media1.giphy.com/media/fnlXXGImVWB0RYWWQj/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp'},
                               {'Title': 'Anti-Gravity Technology',
                                'hemisphere_url': 'https://media1.giphy.com/media/wOJhrjx3lFxh9ShCZY/giphy.webp?cid=790b761122897cf1a00f010852e522814f44989b84eb167c&rid=giphy.webp'},
                               {'Title': 'Advanced Linguistics',
                                'hemisphere_url': 'https://media3.giphy.com/media/WEiKBTaESHHhK/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp'},
                               {'Title': 'Martian Corgi Spacesuit', 'hemisphere_url': 'https://media2.giphy.com/media/RuP38JSfj14je/giphy.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=giphy.webp'}]
            }
    collection.insert_one(post)
    # Verify results:
    results = collection.find_one()
    # for result in results:
    #     print(result)
    return results


#%%
