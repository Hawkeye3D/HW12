# import necessary libraries
import pandas as pd
from flask import Flask, render_template
# %%
# Module used to connect Python with MongoDb
import pymongo
import datetime


# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# declare database
db = client.mars_db  # implicitly declared mars DB
collection_mars_tidbits = db.mars_db

post = {'nasatitle': 'Corgies on Mars'}
# 'nasanote': 'In a surprise development today  a pack of what appear to be cute Corgies were seen roaming an Ancient Alien ruin on Mars. This has completely rattled the scientfic community. Nay sayers claim it is just another example of fake news, but Corgie lovers world-wide say it is proof that Corgies are the best and brightest dog breed.',
# 'nasaimgURL': 'https://media1.giphy.com/media/vGo2sgzeC8r60/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp',
# 'nasadate': datetime.datetime.utcnow(),
# 'jpl_featured_image_url': 'https://media1.giphy.com/media/wOJhrjx3lFxh9ShCZY/giphy.webp?cid=790b761122897cf1a00f010852e522814f44989b84eb167c&rid=giphy.webp',
# 'mars_weather': 'Partly dusty, 70 degrees F'
# }

# 'hemispherepics': [{'Title': 'Water on Mars', 'hemisphere_url': 'https://media1.giphy.com/media/fnlXXGImVWB0RYWWQj/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp'},
# {'Title': 'Anti-Gravity Technology',
#     'hemisphere_url': 'https://media1.giphy.com/media/wOJhrjx3lFxh9ShCZY/giphy.webp?cid=790b761122897cf1a00f010852e522814f44989b84eb167c&rid=giphy.webp'},
# {'Title': 'Advanced Linguistics',
#     'hemisphere_url': 'https://media3.giphy.com/media/WEiKBTaESHHhK/200w.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=200w.webp'},
# {'Title': 'Martian Corgi Spacesuit', 'hemisphere_url': 'https://media2.giphy.com/media/RuP38JSfj14je/giphy.webp?cid=790b76116174feb42843815998a66504ca992d6761f09bc0&rid=giphy.webp'}]


# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def echo():

    return render_template("index.html", date=datestr)


# Bonus add a new route
@app.route("/queryMongo")
def bonus():

    return render_template("bonus.html", date=datestr)


if __name__ == "__main__":
    app.run(debug=True)
