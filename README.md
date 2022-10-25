INITIAL IDEAS

Make a web page of the 400 word list quickly with Python.
- Get the list of words and make into arrays.
- Use pip install googletrans to get translations - see test-googletrans.py - pip install googletrans==3.1.0a0 - WORKING
- Use pip install icrawler to get images of those words - see test.icrawler.py - pip install icrawler - WORKING WITH BING SEARCH
- Generate web page with each card featuring the image, English word and Welsh word.

test001.py: Make page with small array
- Get translations and turn into a saved array
- Get images into a folder named the same as English word





FOLDER initial-tests INCLUDES
- googletrans test
- icrawler test
- all in one file test
- index.html is a test Vue file to display results showing json data and images from test scrape


FOLDER word-lists INCLUDES
- Text document of 625 words with link to website words are taken from - this list used
- Text document of 400 words with link to website words are taken from


MAIN FOLDER INCLUDES
- index.html Vue file that loads the json and creates page of translations with images
- words625-getimages.py uses arrays of words and icrawler to scrape images from Bing image search - Bing used because the icrawler library was erroring when trying to use Google image search, github says it's a known error
- words625-makejson.py uses googletrans to get translation of words in arrays and makes the json file engtocy.json which lists groups, english, cymru and image link

Ended up using two different python files to seperate scraping the images and constructing the json file because there was only a need to scrape images once, whereas I ran the makejson file quite a few times before I got the json formatted as I wanted.

