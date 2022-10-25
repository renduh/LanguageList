from googletrans import Translator
import json
# from icrawler.builtin import BingImageCrawler
import os



animals_eng = ['Animal', 'dog', 'cat', 'fish', 'bird', 'cow', 'pig', 'mouse', 'horse', 'wing']
animals_cy = []
animals_img = []

transport_eng = ['Transportation', 'train', 'plane', 'car', 'truck', 'bicycle', 'bus', 'boat', 'ship', 'tire', 'gasoline', 'engine', 'ticket']
transport_cy = []
transport_img = []

location_eng = ['Location', 'city', 'house', 'apartment', 'street', 'airport', 'station', 'bridge', 'hotel', 'restaurant', 'farm', 'court', 'school', 'office', 'room', 'town', 'university', 'club', 'bar', 'park', 'camp', 'shop', 'theater', 'library', 'hospital', 'church', 'market', 'country', 'building', 'ground', 'space', 'bank']
location_cy = []
location_img = []

clothing_eng = ['Clothing', 'hat', 'dress', 'suit', 'skirt', 'shirt', 'T-shirt', 'pants', 'shoes', 'pocket', 'coat', 'stain']
clothing_cy = []
clothing_img = []

colour_eng = ['Colour', 'red', 'green', 'blue', 'yellow', 'brown', 'pink', 'orange', 'black', 'white', 'gray']
colour_cy = []
colour_img = []

people_eng = ['People', 'son', 'daughter', 'mother', 'father', 'parent', 'baby', 'man', 'woman', 'brother', 'sister', 'family', 'grandfather', 'grandmother', 'husband', 'wife', 'king', 'queen', 'president', 'neighbor', 'boy', 'girl', 'child', 'adult', 'human', 'friend', 'victim', 'player', 'fan', 'crowd']
people_cy = []
people_img = []

job_eng = ['Job', 'Teacher', 'student', 'lawyer', 'doctor', 'patient', 'waiter', 'secretary', 'priest', 'police', 'army', 'soldier', 'artist', 'author', 'manager', 'reporter', 'actor']
job_cy = []
job_img = []

society_eng = ['Society', 'religion', 'heaven', 'hell', 'death', 'medicine', 'money', 'dollar', 'bill', 'marriage', 'wedding', 'team', 'ethnicity', 'sex', 'gender', 'murder', 'prison', 'technology', 'energy', 'war', 'peace', 'attack', 'election', 'magazine', 'newspaper', 'poison', 'gun', 'sport', 'race', 'exercise', 'ball', 'game', 'price', 'contract', 'drug', 'sign', 'science', 'God']
society_cy = []
society_img = []

art_eng = ['Art', 'band', 'song', 'musical' 'instrument', 'music', 'movie']
art_cy = []
art_img = []

beverages_eng = ['Beverages', 'coffee', 'tea', 'wine', 'beer', 'juice', 'water', 'milk']
beverages_cy = []
beverages_img = []

food_eng = ['Food', 'egg', 'cheese', 'bread', 'soup', 'cake', 'chicken', 'pork', 'beef', 'apple', 'banana', 'orange', 'lemon', 'corn', 'rice', 'oil', 'seed', 'knife', 'spoon', 'fork', 'plate', 'cup', 'breakfast', 'lunch', 'dinner', 'sugar', 'salt', 'bottle']
food_cy = []
food_img = []

home_eng = ['Home', 'table', 'chair', 'bed', 'dream', 'window', 'door', 'bedroom', 'kitchen', 'bathroom', 'pencil', 'pen', 'photograph', 'soap', 'book', 'page', 'key', 'paint', 'letter', 'note', 'wall', 'paper', 'floor', 'ceiling', 'roof', 'pool', 'lock', 'telephone', 'garden', 'yard', 'needle', 'bag', 'box', 'gift', 'card', 'ring', 'tool']
home_cy = []
home_img = []

electronics_eng = ['Electronics', 'clock', 'lamp', 'fan', 'mobile phone', 'network', 'computer', 'computer program', 'laptop', 'screen', 'camera', 'television', 'radio']
electronics_cy = []
electronics_img = []

body_eng = ['Body', 'head', 'neck', 'face', 'beard', 'hair', 'eye', 'mouth', 'lip', 'nose', 'tooth', 'ear', 'tear drop', 'tongue', 'back', 'toe', 'finger', 'foot', 'hand', 'leg', 'arm', 'shoulder', 'heart', 'blood', 'brain', 'knee', 'sweat', 'disease', 'bone', 'voice', 'skin']
body_cy = []
body_img = []

nature_eng = ['Nature', 'sea', 'ocean', 'river', 'mountain', 'rain', 'snow', 'tree', 'sun', 'moon', 'world', 'Earth', 'forest', 'sky', 'plant', 'wind', 'soil', 'flower', 'valley', 'root', 'lake', 'star', 'grass', 'leaf', 'air', 'sand', 'beach', 'wave', 'fire', 'ice', 'island', 'hill', 'heat']
nature_cy = []
nature_img = []

materials_eng = ['Materials', 'glass', 'metal', 'plastic', 'wood', 'stone', 'diamond', 'clay', 'dust', 'gold', 'copper', 'silver']
materials_cy = []
materials_img = []

measurements_eng = ['Measurements', 'meter', 'centimeter', 'kilogram', 'inch', 'foot', 'pound', 'half', 'circle', 'square', 'temperature', 'date', 'weight', 'edge', 'corner']
measurements_cy = []
measurements_img = []

nouns_eng = ['Nouns', 'map', 'dot', 'consonant', 'vowel', 'light', 'sound', 'yes', 'no', 'piece', 'pain', 'injury', 'hole', 'image', 'pattern', 'noun', 'verb', 'adjective']
nouns_cy = []
nouns_img = []

directions_eng = ['Directions', 'top', 'bottom', 'side', 'front', 'back', 'outside', 'inside', 'up', 'down', 'left', 'right', 'straight', 'north', 'south', 'east', 'west']
directions_cy = []
directions_img = []

seasons_eng = ['Seasons', 'Summer', 'Spring', 'Winter', 'Fall', 'season']
seasons_cy = []
seasons_img = []

# numbers_eng = ['Numbers', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '30', '31', '32', '40', '41', '42', '50', '51', '52', '60', '61', '62', '70', '71', '72', '80', '81', '82', '90', '91', '92', '100', '101', '102', '110', '111', '1000', '1001', '10000', '100000', 'million', 'billion', '1st', '2nd', '3rd', '4th', '5th', 'number']
numbers_eng = ['Numbers', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fiftenn', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'thirty', 'thirty-one', 'thirty-two', 'fourty', 'fourty-one', 'fourty-two', 'fifty', 'fifty-one', 'fifty-two', 'sixty', 'sixty-one', 'sixty-two', 'seventy', 'seventy-one', 'seventy-two', 'eighty', 'eighty-one', 'eighty-two', 'ninety', 'ninety-one', 'ninety-two', 'one hundred', 'one hundred and one', 'one hundred and two', 'one hundred and ten', 'one hundred and eleven', 'one thousand', 'one thousand and one', 'ten thousand', 'one hundred thousand', 'million', 'billion', 'first', 'second', 'third', 'fourth', 'fifth', 'number']
numbers_cy = []
numbers_img = []

months_eng = ['Months', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_cy = []
months_img = []

daysoftheweek_eng = ['Days of the week', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daysoftheweek_cy = []
daysoftheweek_img = []

time_eng = ['Time', 'year', 'month', 'week', 'day', 'hour', 'minute', 'second', 'morning', 'afternoon', 'evening', 'night']
time_cy = []
time_img = []

verbs_eng = ['Verbs', 'work', 'play', 'walk', 'run', 'drive', 'fly', 'swim', 'go', 'stop', 'follow', 'think', 'speak', 'say', 'eat', 'drink', 'kill', 'die', 'smile', 'laugh', 'cry', 'buy', 'pay', 'sell', 'shoot', 'learn', 'jump', 'smell', 'hear', 'listen', 'taste', 'touch', 'see', 'watch TV', 'kiss', 'burn', 'melt', 'dig', 'explode', 'sit', 'stand', 'love', 'pass by', 'cut', 'fight', 'lie down', 'dance', 'sleep', 'wake up', 'sing', 'count', 'marry', 'pray', 'win', 'lose', 'mix', 'stir', 'bend', 'wash', 'cook', 'open', 'close', 'write', 'call', 'turn', 'build', 'teach', 'grow', 'draw', 'feed', 'catch', 'throw', 'clean', 'find', 'fall', 'push', 'pull', 'carry', 'break', 'wear', 'hang', 'shake', 'sign', 'beat', 'lift']
verbs_cy = []
verbs_img = []

adjectives_eng = ['Adjectives', 'long', 'short', 'tall', 'wide', 'narrow', 'big', 'large', 'small', 'little', 'slow', 'fast', 'hot', 'cold', 'warm', 'cool', 'new', 'old', 'new', 'young', 'good', 'bad', 'wet', 'dry', 'sick', 'healthy', 'loud', 'quiet', 'happy', 'sad', 'beautiful', 'ugly', 'deaf', 'blind', 'nice', 'mean', 'rich', 'poor', 'thick', 'thin', 'expensive', 'cheap', 'flat', 'curved', 'male', 'female', 'tight', 'loose', 'high', 'low', 'soft', 'hard', 'deep', 'shallow', 'clean', 'dirty', 'strong', 'weak', 'dead', 'alive', 'heavy', 'light', 'dark', 'nuclear', 'famous']
adjectives_cy = []
adjectives_img = []

pronouns_eng = ['Pronouns', 'I', 'you', 'he', 'she', 'it', 'we', 'you', 'they']
pronouns_cy = []
pronouns_img = []



allarrays = ['animals_eng', 'transport_eng', 'location_eng', 'clothing_eng', 'colour_eng', 'people_eng', 'job_eng', 'society_eng', 'art_eng', 'beverages_eng', 'food_eng', 'home_eng', 'electronics_eng', 'body_eng', 'nature_eng', 'materials_eng', 'measurements_eng', 'nouns_eng', 'directions_eng', 'seasons_eng', 'numbers_eng', 'months_eng', 'daysoftheweek_eng', 'time_eng', 'verbs_eng', 'adjectives_eng', 'pronouns_eng']
# allarrays = ['animals_eng', 'transport_eng']


translator = Translator()
json_list = []

for array in allarrays:
  firstword=eval(array)[0]
  wordlist_eng = []

  translations = translator.translate(eval(array), dest='cy')
  translated_list = []
  image_list = []
  for translation in translations:
    wordlist_eng.append(translation.origin)
    translated_list.append(translation.text)
    newsavename = 'img625/' + firstword + '-' + translation.origin + '.jpg'
    image_list.append(newsavename)

  print(firstword)
  print(wordlist_eng)
  print(translated_list)
  print(image_list)

  thegroup = []
  for index, entry in enumerate(eval(array)):
    wordinfo = {'english': wordlist_eng[index], 'cymru': translated_list[index], 'image': image_list[index] }
    thegroup.append(wordinfo)
  maingroup = {"group": firstword, "words": thegroup}
  json_list.append(maingroup)


json_string = json.dumps(json_list, indent = 2)  
with open("engtocy.json", "w") as outfile:
  outfile.write(json_string)