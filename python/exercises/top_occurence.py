import requests
#if you use an IDE, do not forget to install the requests module in the Command Line, this way:
#pip install requests
import re
import json

def removeHTMLtags(textWithHTMLTags):
  textWithoutHTML=re.sub("<.*?>","",textWithHTMLTags)
  return textWithoutHTML

result = requests.get('http://shakespeare.mit.edu/romeo_juliet/full.html')
#knowing that the source of the web page does not contain "<" and ">" characters for other purposes than HTML tags
resultedText=removeHTMLtags(result.text)

wordList=resultedText.split()[30:]
# print(wordList)
pattern = r'[^A-Za-z0-9]+'
# sample_str = re.sub(pattern, '', sample_str)
wordFreq = {}
for word in wordList:
  word = re.sub(pattern,'',word).rstrip(',')
  wordFreq[word]=wordList.count(word)
# print(wordFreq)
values=list(wordFreq.values())
values.sort()
values = values[-20:]
print('top 20 occurences: ', values[-20:])
dictResult = {}
for (k, item) in wordFreq.items():
    if item in values:
      dictResult[k] = item
print('Top 20 words with highest occurence')
print(json.dumps(dictResult, indent=2))