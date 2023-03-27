import requests
# if you use an IDE, do not forget to install the requests module in the Command Line, this way:
# pip install requests
import re


def removeHTMLtags(textWithHTMLTags):
    textWithoutHTML = re.sub("<.*?>", "", textWithHTMLTags)
    return textWithoutHTML


def fileDetails(startDict, line):
    for ch in line:
        startDict[ch] = line.count(ch)
    sorted_dict = {k: v for k, v in sorted(startDict.items(), key=lambda item: item[1], reverse=True)}
    top_items = list(sorted_dict.items())[:3]
    last_items = list(sorted_dict.items())[-3:]
    print('Top 3 most used commands: ')
    for item, value in top_items:
        print(f"{item}: {value}")
    print('Top 3 least used commands: ')
    for item, value in last_items:
        print(f"{item}: {value}")


def writeAndClose(item):
    f = open('../files/words.txt', 'a')
    f.write(item)
    f.close()


def openAndRead(nrOfLine):
    f = open('../files/words.txt', 'r')
    line = f.readlines()[nrOfLine]
    f.close()
    return line


result = requests.get('http://shakespeare.mit.edu/romeo_juliet/full.html')
# knowing that the source of the web page does not contain "<" and ">" characters for other purposes than HTML tags
resultedText = removeHTMLtags(result.text)

wordList = resultedText.split()[30:]
# print(wordList[10:20])
filteredList = []
startDict = {}
f = open('../files/words.txt', 'w+')
startCh = input("All words that starts with: ")
writeAndClose(startCh)
while startCh.lower() != 'stop':
    for word in wordList:
        if word.startswith(startCh):
            filteredList.append(word)
    fileDetails(startDict, openAndRead(0))
    startCh = input("All words that starts with: ")
    if startCh.lower() != 'stop':
        writeAndClose(startCh)

print('All words that starts with:', startCh, filteredList)

filteredList.clear()
writeAndClose('\n')
startDict.clear()
endCh = input("All words that ends with: ")
if endCh.lower() != 'stop':
    writeAndClose(endCh)
while endCh.lower() != 'stop':
    for word in wordList:
        if word.endswith(endCh):
            filteredList.append(word)
    fileDetails(startDict, openAndRead(1))
    endCh = input("All words that ends with: ")
    if endCh.lower() != 'stop':
        writeAndClose(endCh)
# print('All words that end with:', endCh, filteredList)
