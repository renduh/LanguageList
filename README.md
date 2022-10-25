# Auto-generating language learning cards

I'm learning Welsh and I came across a few articles saying learning a base of a few hundred words is a good way to go. The lists of words were online but I wanted a quick way to make that list into a web page with cards.

I ended up using a couple of python libraries to scrape images and scrape translations. The images in particular are a bit hit and miss. I wrote two python scripts to use those libraries and get things as I wanted them, exporting everything to a json file.

All I had to do then was write a quick html file (I actually used Vue to run through the json) to display the results. 

Feel free to use or change, if you're learning a differnet language, you'd only have to change from Welsh (cy) to another langulage and run the script to make a whole new set of cards.

#### Python libraries used
- pip install googletrans==3.1.0a0
- pip install icrawler

#### FOLDER initial-tests INCLUDES
- googletrans test
- icrawler test
- all in one file test
- index.html is a test Vue file to display results showing json data and images from test scrape

#### FOLDER word-lists INCLUDES
- Text document of 625 words with link to website words are taken from (https://method.fluent-forever.com/base-vocabulary-list/) - this list used
- Text document of 400 words with link to website words are taken from (https://fastlanguagemastery.com/400-most-common-words/)

#### MAIN FOLDER INCLUDES
- index.html Vue file that loads the json and creates page of translations with images
- words625-getimages.py uses arrays of words and icrawler to scrape images from Bing image search - Bing used because the icrawler library was erroring when trying to use Google image search, github says it's a known error
- words625-makejson.py uses googletrans to get translation of words in arrays and makes the json file engtocy.json which lists groups, english, cymru and image link

Ended up using two different python files to seperate scraping the images and constructing the json file because there was only a need to scrape images once, whereas I ran the makejson file quite a few times before I got the json formatted as I wanted.

Some of the scraped images can be strange because I set the library to just download the first image result. Could go in and manually download some better images for a few things but tbh, I quite like the weird image choices. Some of them I don't like though, especially ones relating to words like ugly etc.



==========================================================================


INITIAL IDEAS

I've left this here for me really, these are a few notes I made before I started and along the way.

Make a web page of the 400 word list quickly with Python.
- Get the list of words and make into arrays.
- Use pip install googletrans to get translations - see test-googletrans.py - pip install googletrans==3.1.0a0 - WORKING
- Use pip install icrawler to get images of those words - see test.icrawler.py - pip install icrawler - WORKING WITH BING SEARCH
- Generate web page with each card featuring the image, English word and Welsh word.

test001.py: Make page with small array
- Get translations and turn into a saved array
- Get images into a folder named the same as English word