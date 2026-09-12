def count_lines_and_words(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    line_count = len(lines)
    word_count = 0

    for line in lines:
        word_count += len(line.split())

    print(f"No. of lines: {line_count}")
    print(f"No. of words: {word_count}")


count_lines_and_words("day_19/obama_speech.txt")
count_lines_and_words("day_19/melina_trump_speech.txt")
count_lines_and_words("day_19/donald_speech.txt")
count_lines_and_words("day_19/michelle_obama_speech.txt")

import json
def language_count(z):
 with open("./day_19/countries_data.json",encoding="utf-8") as f:
    data = json.load(f)
    language_count={}
    for countries in data:
        languages=countries["languages"]
        for language in languages:
         if language in language_count:
             language_count[language]+=1
         else:
             language_count[language]=1
 x=sorted(language_count.items(),reverse=True,key=lambda x:x[1])
 y=x[:z]
 return y


print(language_count(11))   

def population_count(z):
 with open("./day_19/countries_data.json",encoding="utf-8") as f:
    data = json.load(f)
    population_count={}
    for countries in data:
        population_count[countries["name"]]=countries['population']
 x=sorted(population_count.items(),reverse=True,key=lambda x:x[1])
 y=x[:z]
 return y

print(population_count(10))

import re

with open("./day_19/email_exchange_big.txt") as f:
   x=f.read()
   emails=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',x)

   print(emails)

with open("./day_19/sample.txt") as f:
   y=f.read()
   z=y.lower()
   a=z.split()
   word_count_dict={}
   word_count_list=list()

   for word in a:
      b=word.strip("?.,!:;")
      if b in word_count_dict:
       word_count_dict[b]+=1
      else:
       word_count_dict[b]=1
for key,value in word_count_dict.items():
   word_count_list.append((value,key))
word_count_list.sort(reverse=True)   
print(word_count_list)

def most_frequent_words(pathname):
   with open(pathname) as f:
      x=f.read().lower().split()
      frequent_word_dict={}
      for word in x:
         y=word.strip(":;,.?!")
         if y in frequent_word_dict:
            frequent_word_dict[y]+=1
         else:
            frequent_word_dict[y]=1
      z=sorted(frequent_word_dict.items(),reverse=True,key=lambda x:x[1])
      z=z[:10]
   print(z)  
         
most_frequent_words("day_19/donald_speech.txt")     

from stop_words import stop_words
def check_text_similarity(pathname1,pathname2):
   with open(pathname1) as f:
    y=f.read().lower().split()

   with open(pathname2) as f:
       x=f.read().lower().split()

   cleaned_words_1=[]
   for word in y:
      a=word.strip(":;,.?!")
      if a not in stop_words:
         cleaned_words_1.append(a)

   cleaned_words_2=[]
   for word in x:
         a=word.strip(":;,.?!")
         if a not in stop_words:
            cleaned_words_2.append(a)
   set_1 = set(cleaned_words_1)
   set_2 = set(cleaned_words_2)
   common_words=set_1.intersection(set_2)
   unique_words=set_1.union(set_2)
   no_common_words=len(common_words)
   no_unique_words=len(unique_words)
   return f'the text similarity is {(no_common_words/no_unique_words)*100} percent'

print(check_text_similarity("./day_19/donald_speech.txt","day_19/melina_trump_speech.txt"))

import csv
with open("day_19/hacker_news.csv") as f:
   reader=csv.reader(f)
   count=0
   count_javascript=0
   count_java=0
   for row in reader:
      x=row[1]
      x=x.lower()
      if "python" in x:
         count+=1

      if "javascript" in x:
         count_javascript+=1 

      if "java" in x and "javascript" not in x:
         count_java+=1     
print(count)   
print(count_javascript)           
print(count_java) 

    

