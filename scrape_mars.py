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
import os
# RAW DATA SOURCE
def dprint(flag,str):
    '''
    Purpose:Debug Print
    flag:set to True if output is desired
    str: item to print
    '''
    if flag:
        print(str)

def dpprint(flag,str):
    '''
    Purpose:Debug Print
    flag:set to True if output is desired
    str:item to print
    '''
    if flag:
        pp.pprint(str)
 
def SetSources():
    ''' Returns a dictionary of the websites
     to be scraped '''
    URL_DataSources={}
   
    URL_DataSources.update({'NASA':'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'})
    URL_DataSources.update({'JPL':'https://www.jpl.nasa.gov/spaceimages/'})
    URL_DataSources.update({'Mars Weather': 'https://twitter.com/MarsWxReport'})
    URL_DataSources.update({'Mars Facts': 'https://space-facts.com/mars/'})
    URL_DataSources.update({'Hemispheres': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'})
    return URL_DataSources
#URLS=SetSources()

def scrape_mars_info():
    ''' This will scrape all the sites that are in the SetSources'''
    URLS=SetSources()
    
    for n in URLS:
        if n =='NASA':
            # Connect to the URL using urllib request
            response= requests.get(URLS[n] )
            soup = bs(response.text, 'lxml')
            allcontents = soup.find_all('div', "content_title" )
            allteasers = soup.find_all('div','rollover_description_inner')            
            retcontent= allcontents[0].text.strip()
            retteaser=  allteasers[0].text.strip()
            retimage = "mars.jpg"
        elif n == 'JPL':
            response= requests.get(URLS[n] )
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
            response= requests.get(URLS['Mars Weather'] )
            soup = bs(response.text, 'lxml')    
            retweather = soup.find('div','js-tweet-text-container').text #,'js-tweet-text-container')
            #dprint(printflag,retweather )
        elif n=='Mars Facts':
            response= requests.get(URLS['Mars Facts'] )
            soup = bs(response.text, 'lxml') 
            retdata= soup.find_all('table')
            rethtmltable0=retdata[0]
            rethtmltable1=retdata[1]
        elif n=='Hemispheres':
            response= requests.get(URLS['Hemispheres'] )
            soup = bs(response.text, 'lxml') 
            
            # This gives us the four blocks of data associated with each picture
            retpics = soup.find_all('div', class_='item')
            
            #Each of the above blocks needs to be scraped of an image href, a description I will use as a popup, and a url to where the image is, on aonther web page
            popups=[]
            imgurls=[]
            
            #loop throught the web pages, get popup text for pictures and get webpage of picture
            for item in retpics:
                popups.append(item.text)
                imgurls.append(urljoin(URLS['Hemispheres'],item.find('a').get('href')))
                
            rethemiimgs =[] # return list of image addresses
            rethemicaptions =[] # Caption to place under image
            rethemisubcaptions =[] #Source of image caption
            rethemidict=[]
            for item in imgurls:
                time.sleep(1)
                response= requests.get(item)
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
    'nasaimgURL': retimage,
    'nasacardimage': retimage,
    'nasadate': datetime.datetime.utcnow(),
    'datatable1':rethtmltable0,
    'datatable2':rethtmltable1,
    'jpl_featured_image_url': retpicofday,
    'mars_weather': retweather,
    'popups':popups,
    'hemispherepics':rethemidict
    }
    return post #dictionary of update
    #collection.insert_one(post)       