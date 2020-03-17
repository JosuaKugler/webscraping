from synonyms import main as synonyms
import random

text = "Rui tut Schlittschuh laufen lieben"

textlist = text.split(" ")
textdict = {}

for word in textlist:
    textdict[word] = synonyms(word)

actualtextdict = {}
for word in textdict:
    if textdict[word] != []:
        actualtextdict[word] = textdict[word][random.randint(0, len(textdict[word]))]
    else:
        actualtextdict[word] = word

text = ""
for word in textdict:
    text = text + actualtextdict[word] + " "

print(text)