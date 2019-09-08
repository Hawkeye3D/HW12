from flask import Flask, render_template, redirect
# %%
# Module used to connect Python with MongoDb

from flask_pymongo import PyMongo
import pandas as pd
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


app = Flask(__name__)

# The default port used by MongoDappB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# declare database
db = client.mars_db  # implicitly declared mars DB
collection = db.mars_db

# This is run when the web page opens;f
@app.route("/")
def home():
    SetupMarsDB(False)
    mars_data = collection.find_one()
    return render_template("index.html", marsdata=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = scrape_mars_info()
    # Update the Mongo database using update and upsert=True
    db.collection.update({}, mars_data, upsert=True)
    # Redirect back to home page
    return redirect("/")


def SetupMarsDB(CorgiFlag):
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

    if CorgiFlag:
        post = {'nasatitle': 'CORGIES ROAMING MARS!!',
                'nasanote': 'In a surprise development today  a pack of what appear to be cute Corgies were seen roaming an Ancient Alien ruin on Mars. This has completely rattled the scientfic community. Nay sayers claim it is just another example of fake news, but Corgie lovers world-wide say it is proof that Corgies are the best and brightest dog breed.',
                'nasaimgURL': 'https://media1.giphy.com/media/vGo2sgzeC8r60/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp',
                'nasacardimage': '',
                'nasadate': datetime.datetime.utcnow(),
                'jpl_featured_image_url': 'https://media1.giphy.com/media/wOJhrjx3lFxh9ShCZY/giphy.webp?cid=790b761122897cf1a00f010852e522814f44989b84eb167c&rid=giphy.webp',
                'mars_weather': 'Partly dusty, 70 degrees F, Raining Mainly Corgis in the Plains',
                'popups': ['1', '2', '3', '4'],
                'hemispherepics': [{'Title': 'Water on Mars', 'hemisphere_url': 'https://media1.giphy.com/media/fnlXXGImVWB0RYWWQj/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp'},
                                {'Title': 'Anti-Gravity Technology',
                                    'hemisphere_url': 'https://media1.giphy.com/media/wOJhrjx3lFxh9ShCZY/giphy.webp?cid=790b761122897cf1a00f010852e522814f44989b84eb167c&rid=giphy.webp'},
                                {'Title': 'Advanced Linguistics',
                                    'hemisphere_url': 'https://media3.giphy.com/media/WEiKBTaESHHhK/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp'},
                                {'Title': 'Martian Corgi Spacesuit', 'hemisphere_url': 'https://media2.giphy.com/media/RuP38JSfj14je/giphy.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=giphy.webp'}],
                'marsurls': collectsetsources()
                }
    else:  # scrape information
        post = scrape_mars_info()

    collection.insert_one(post)
    # Verify results:
    results = collection.find_one()
    # for result in results:
    #     print(result)
    return results


def SetSources():
    ''' Returns a dictionary of the websites
    to be scraped '''
    URL_DataSources = {}

    URL_DataSources.update(
        {'NASA': 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'})
    URL_DataSources.update({'JPL': 'https://www.jpl.nasa.gov/spaceimages/'})
    URL_DataSources.update(
        {'Mars Weather': 'https://twitter.com/MarsWxReport'})
    URL_DataSources.update({'Mars Facts': 'https://space-facts.com/mars/'})
    URL_DataSources.update(
        {'Hemispheres': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'})
    return URL_DataSources
# URLS=SetSources()


def collectsetsources():
    '''Return a List of dictionary listings'''
    cscs = []
    urls = SetSources()
    for url in urls:
        cscs.append(url)
    return cscs


def scrape_mars_info():
    ''' This will scrape all the sites that are in the SetSources'''
    URLS = SetSources()

    for n in URLS:
        if n == 'NASA':
            # Connect to the URL using urllib request
            try:
                response = requests.get(URLS[n], timeout=10)
            except requests.exceptions.Timeout:
                pass    
            soup = bs(response.text, 'lxml')
            allcontents = soup.find_all('div', "content_title")
            allteasers = soup.find_all('div', 'rollover_description_inner')
            retcontent = allcontents[0].text.strip()
            retteaser = allteasers[0].text.strip()
            retimage = ""
        elif n == 'JPL':
            try:
                response= requests.get(URLS[n], timeout=10 )
            except requests.exceptions.Timeout:
                pass    
            soup = bs(response.text, 'lxml')        
            bigpicofday=soup.find_all('a', 'fancybox', id='full_image' ) 
            strstr=str(bigpicofday[0])#convert string to string for some pythonic reason
            strt =(strstr.find('data-fancybox-href'))
            lsubstr=len('data-fancybox-href="')#include the quote
            newstr=strstr[lsubstr+strt:-1].split(" ")[0]  
            newstr=urljoin(URLS['JPL'], newstr)
            newstr=newstr[0:len(newstr)-1]
            retpicofday=(urljoin(URLS['JPL'], newstr)) 
           # dprint(printflag,"JPL Pic of day: "+retpicofday)
        elif n=='Mars Weather':
            try:
                response= requests.get(URLS['Mars Weather'], timeout=10 )
            except requests.exceptions.Timeout:
                pass    
            soup = bs(response.text, 'lxml')    
            retweather = soup.find('div','js-tweet-text-container').text #,'js-tweet-text-container')
            # dprint(printflag,retweather )
        elif n=='Mars Facts':
            try:
                response= requests.get(URLS['Mars Facts'], timeout=10 )
            except requests.exceptions.Timeout:
                pass
            soup = bs(response.text, 'lxml') 
            retdata= soup.find_all('table')
            # retdata[1].columns=['Parameter Description','Value']
            rethtmltable1=str(retdata[1])
            rethtmltable0=str(retdata[0])

        elif n=='Hemispheres':
            try:
                response= requests.get(URLS['Hemispheres'], timeout=10 )
            except requests.exceptions.Timeout:
                pass    
            soup = bs(response.text, 'lxml') 
            
            # This gives us the four blocks of data associated with each picture
            retpics = soup.find_all('div', class_='item')
            
            # Each of the above blocks needs to be scraped of an image href, a description I will use as a popup, and a url to where the image is, on aonther web page
            popups=[]
            imgurls=[]
            
            # loop throught the web pages, get popup text for pictures and get webpage of picture
            for item in retpics:
                popups.append(item.text)
                imgurls.append(urljoin(URLS['Hemispheres'],item.find('a').get('href')))
                
            rethemiimgs =[] # return list of image addresses
            rethemicaptions =[] # Caption to place under image
            rethemisubcaptions =[] #Source of image caption
            rethemidict=[]
            for item in imgurls:
                time.sleep(1)
                try:
                    response= requests.get(item,timeout=10)
                except requests.exceptions.Timeout:
                    pass                      
                soup = bs(response.text, 'lxml')
                image=urljoin(item, soup.find('img',class_='wide-image').get('src'))
                rethemiimgs.append(image)
                titles=soup.title.text.split('|')
                rethemicaptions.append(titles[0].replace(' Enhanced ',""))
                rethemisubcaptions.append(titles[1].strip())
                rethemidict.append({'title':titles[0],'img_url':image})
               
            # dprint(printflag,rethemicaptions)
            # dprint(printflag,rethemisubcaptions)
            # dpprint(printflag,rethemiimgs) 
            # dprint(printflag,rethemidict)
 
    post = {'nasatitle': retcontent,
    'nasanote': retteaser,
    'nasaimgURL': retpicofday,#retimage,
    'nasacardimage': retpicofday,#retimage,
    'nasadate': datetime.datetime.utcnow(),
    'datatable1':rethtmltable0,
    'datatable2':rethtmltable1,
    'jpl_featured_image_url': retpicofday,
    'mars_weather': retweather,
    'popups':popups,
    'hemispherepics':rethemidict
    }
    return post #dictionary of update

if __name__ == "__main__":
    app.run()


# %%
