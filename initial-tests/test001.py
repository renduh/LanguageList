from googletrans import Translator
import json
from icrawler.builtin import BingImageCrawler
import os

# arrays for english, welsh and images
animals_eng = ['Animal', 'dog', 'cat', 'fish', 'bird', 'cow', 'pig', 'mouse', 'horse', 'wing']
animals_cy = []
animals_img = []

# start the translator and loop through english words
translator = Translator()
translations = translator.translate(animals_eng, dest='cy')
for translation in translations:
	# add translation to welsh array
	animals_cy.append(translation.text)
	print(translation.origin, ' -> ', translation.text)
	# get an image of english word, rename it to that english word, add image path to image array
	google_crawler = BingImageCrawler(storage={'root_dir': 'img'})
	google_crawler.crawl(keyword=translation.origin, max_num=1)
	newsavename = 'img/' + translation.origin + '.jpg'
	os.rename('img/000001.jpg', newsavename)
	animals_img.append(newsavename)


print(animals_cy)

# combine those arrays into a dictionary
case_list = []
for index, entry in enumerate(animals_eng):
    case = {'english': animals_eng[index], 'cymru': animals_cy[index], 'image': animals_img[index] }
    case_list.append(case)

# convert dictionary to json and save as a file
json_string = json.dumps(case_list, indent = 2)  
print(json_string)  
with open("data.json", "w") as outfile:
    outfile.write(json_string)
















# This bit saves an image

# from icrawler.builtin import BingImageCrawler

# google_crawler = BingImageCrawler(storage={'root_dir': 'img'})
# google_crawler.crawl(keyword='cat', max_num=1)

# import os

# os.rename('img/000001.jpg', 'img/cat.jpg')





# This is working for saving a json file

# import json  
  
# fields=["eng", "cy", "img"]  
# values=["Alice", "female", 30 ]  
  
# dic = {fields[i]: values[i] for i in range (len(fields))}  
  
# json_string = json.dumps(dic, indent = 2)  
  
# print(json_string)  

# with open("data.json", "w") as outfile:
#     outfile.write(json_string)

