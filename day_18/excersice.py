import re
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\b\w+\b', paragraph.lower())
counts = Counter(words)
spoken=list()
for word,count in counts.most_common():
    spoken.append((count,word))
print(spoken)    

paragraph='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
x= [int(x) for x in  re.findall(r'-?\d+',paragraph)]
max=max(x)
min=min(x)
print(max)
print(min)
print(max-(min))
def is_valid_variable(name):
 pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
 return bool(re.match(pattern, name))

print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve t%heching. 
T%he 30 days of y@thon. 
is %%the best. 
thi%s is the challenge'''
cleaned_text = re.sub(r'[^a-zA-Z ]', '', sentence)
words = cleaned_text.lower().split()
word_counts = Counter(words)


print(word_counts.most_common(3))
