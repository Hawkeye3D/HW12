from splinter import Browser
from bs4 import BeautifulSoup
import os
# RAW DATA SOURCE

URL_DateSources =[{'Source':'NASA','URL':'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'},
{'Source':'JPL','URL':'https://www.jpl.nasa.gov/spaceimages/'},
{'Source':'Mars Weate\her','URL':' {'Source':'JPL','URL':'https://twitter.com/MarsWxReport'},
{'Source':'Mars Facts','URL':'https://space-facts.com/mars/'},
{'Source':'Hemispheres','URL':'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'}]
# EXAMPLE ONE

# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     #executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
#     executable_path = {"executable_path": "chromedriver.exe"}
#     return Browser("chrome", **executable_path, headless=False)


# def scrape():
#     browser = init_browser()
#     listings = {}

#     url = "https://raleigh.craigslist.org/search/hhh?max_price=1500&availabilityMode=0"
#     browser.visit(url)

#     html = browser.html
#     soup = BeautifulSoup(html, "html.parser")

#     listings["headline"] = soup.find("a", class_="result-title").get_text()
#     listings["price"] = soup.find("span", class_="result-price").get_text()
#     listings["hood"] = soup.find("span", class_="result-hood").get_text()

#     return listings

# EXAMPLE TWO

    
# def scrape_info():
#     browser = init_browser()

#     # Visit visitcostarica.herokuapp.com
#     url = "https://visitcostarica.herokuapp.com/"
#     browser.visit(url)

#     time.sleep(1)

#     # Scrape page into Soup
#     html = browser.html
#     soup = bs(html, "html.parser")

#     # Get the average temps
#     avg_temps = soup.find('div', id='weather')

#     # Get the min avg temp
#     min_temp = avg_temps.find_all('strong')[0].text

#     # Get the max avg temp
#     max_temp = avg_temps.find_all('strong')[1].text

#     # BONUS: Find the src for the sloth image
#     relative_image_path = soup.find_all('img')[2]["src"]
#     sloth_img = url + relative_image_path

#     # Store data in a dictionary
#     costa_data = {
#         "sloth_img": sloth_img,
#         "min_temp": min_temp,
#         "max_temp": max_temp
#     }

#     # Close the browser after scraping
#     browser.quit()

#     # Return results
#     return costa_data
