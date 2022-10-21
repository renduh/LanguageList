
from googletrans import Translator

translator = Translator()
translations = translator.translate(['Animal', 'dog', 'cat', 'fish', 'bird', 'cow', 'pig', 'mouse', 'horse', 'wing'], dest='cy')
for translation in translations:
  print(translation.origin, ' -> ', translation.text)



