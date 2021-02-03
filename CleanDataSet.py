import pandas as pd
import numpy as np
import csv
import re
# To load the fields list
import fields
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji

fieldsFilter = fields.fields

fileN = "dataFrame2.csv"
dataFrame = pd.read_csv(fileN)

def remove_emoticons(text):
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')
    return emoticon_pattern.sub(r'', text)

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_urls(text):
    result = re.sub(r"http\S+", "", text)
    return(result)

def remove_twitter_urls(text):
    clean = re.sub(r"pic.twitter\S+", "",text)
    return(clean)

def give_emoji_free_text(text):
    return emoji.get_emoji_regexp().sub(r'', text)


dataFrame

print (dataFrame['tweet.full_text'].head())

#Remove libe breaks
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].str.replace('\n','')
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].str.replace('\r','')

#Text cleaning remove urls emoji ...
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].apply(lambda x : remove_urls(x))
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].apply(lambda x : remove_twitter_urls(x))
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].apply(lambda x : remove_emoticons(x))
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].apply(lambda x : remove_emoji(x))
dataFrame['tweet.full_text'] = dataFrame['tweet.full_text'].apply(lambda x : give_emoji_free_text(x))

print (dataFrame['tweet.full_text'].head())

#Save the result in FileName+Clean.csv
with open(fileN[:-5]+"Clean.csv",'w') as write_csv:
    write_csv.write(dataFrame.to_csv(sep=',', index=False))

write_csv.close()