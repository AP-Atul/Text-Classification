import os

import pandas as pd
from tqdm import tqdm

# contents to ignore from the text
ignoreList = [' ', '-', '.', '', '\n', '·', '/', '‏‏‎U+0020‎‎‎‎‎']

# read the headlines directory
dirs = os.listdir("storage/headlines")
print(dirs)
allHeadLines = []

# to keep tr
wordDict = dict()

for file in tqdm(dirs):
    with open(os.path.join("storage/headlines", file), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(".", '').replace("\n", '').replace('=', ' ').replace('| ', '').replace(':', '').replace("\"", "").strip()
            words = line.split(" ")
            for word in words:
                if word in ignoreList:
                    continue
                if wordDict.__contains__(word):
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1

            allHeadLines.append(line)


wordDict = {key: value for key, value in sorted(wordDict.items(), key=lambda item: item[1], reverse=True)}
stopWords = []
count = 0
for key, value in wordDict.items():
    if count > 100:
        break
    print(f"{key} --> {value}")
    stopWords.append(key)
    count += 1

# stop words removing and stemming is unnecessary as we dont have
# lots of data to refine
df = pd.DataFrame({'stop_words': stopWords})
df.to_csv("stopwords.csv", index=False)
print("\n\nStop words csv written...........")

# building the csv file with labels and headlines
lenA = len(allHeadLines) / 3
allLabels = ['maharashtra'] * int(lenA) + ['bollywood'] * int(lenA) + ['sports'] * int(lenA)

print(f"Total Headlines :: {len(allHeadLines)}")
print(f"Total Labels :: {len(allLabels)}")
print(f"Total unique Words :: {len(wordDict)}")

# saving to a csv file
df = pd.DataFrame({'headline': allHeadLines, 'labels': allLabels})
print(f"Shape of df :: {df.shape}")
df.to_csv('marathi_news_headlines', index=False)
print("CSV file created ......................")

# Total Headlines :: 8493
# Total Labels :: 8493
# Total unique Words :: 24719
