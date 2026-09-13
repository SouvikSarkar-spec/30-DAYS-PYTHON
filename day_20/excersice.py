import requests
import string
url="https://raw.githubusercontent.com/GITenberg/The-Tragedy-of-Romeo-and-Juliet_1112/master/1112.txt?utm_source=chatgpt.com"
response=requests.get(url)
txt=response.text
x=txt.lower().split()
dict_words={}

for words in x:
    word=words.strip(string.punctuation)
    if word in dict_words:
        dict_words[word]+=1
    else:
        dict_words[word]=1
y=sorted(dict_words.items(),key=lambda x:x[1],reverse=True)
print(y[:10])        