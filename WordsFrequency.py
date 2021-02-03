import pandas as pd
from collections import Counter
#import matplotlib.pyplot as plt

nb_words_Key = "30"

df = pd.read_csv('dataFrameClean.csv')

result = Counter(" ".join(df['tweet.full_text'].values.tolist()).split(" ")).items()
df2 = pd.DataFrame(result)
df2.columns =['Word', 'Frequency']
df2 = df2[df2.Word != ""] #Deletes the empty spaces counted
df2 = df2.sort_values(['Frequency'], ascending=[False]) #Sort dataframe by frequency (Descending)

print('\033[1mTop '+nb_words_Key+' most words used from the dataset\033[0m \n')
print(df2.head(int(nb_words_Key)).to_string(index=False)) #Prints the top N unique words used


#print("\n")
#df3 = df2.head(int(nb_words_Key))
#df3.plot(y='Frequency', kind='pie', labels=df3['Word'], figsize=(9, 9), autopct='%1.1f%%', title='Top '+nb_words_Key+' most unique words used from the dataset')