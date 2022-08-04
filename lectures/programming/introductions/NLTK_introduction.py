# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:43:45 2017

@author: Alexander Hillert, Goethe University Frankfurt
"""


# import modules
# if you need to download the nltk packages 'punkt' and 'stopwords' you can use
# the following three commands:
#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')


from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

################
# 1. Tokenize
################
# Create a test text to see how well nltk.tokenize performs
test_text="Microsoft Corp. announced they would acquire Yahoo! for $3.4 to prevent Google Inc. \
from taking over Software Ltd. headerquartered in St. Louis. XYZ S.A. is located in the \
U.S. and run by Dr. John P. Smith, who likes short-term risk-based calculations."

# Tokenize sentences
sentence_list=sent_tokenize(test_text)
print("This is the list of sentences:")
print(sentence_list)
# looks good. Only the split after "Yahoo" is incorrect. The tool correctly
# recognizes "Mr.", "Dr.", "Inc.", etc. -> good performance
 
# Tokenize words
word_list=word_tokenize(test_text)
print("This is the list of words:")
print(word_list)
print(len(word_list))
# --> word_tokenize also includes symbols and numbers as words.

# How to delete the elements that are not real words?
word_list_1=[]
for word in word_list:
    if re.search('[A-Za-z]',word):
        word_list_1.append(word)
print("This is the edited list of words. There should be only 'real' words:")
print(word_list_1)
print(len(word_list_1))

# Alternative
test_text1=re.sub('[^A-Za-z\s\n]','',test_text)
word_list_2=word_tokenize(test_text1)
print("This is the edited list of words. There should be only 'real' words:")
print(word_list_2)
print(len(word_list_2))


################
# 2. Stop Words
################
example_sentence = "This is an example showing off stop word filtering."
stop_words=set(stopwords.words("english"))
print("This is the list of stop words from NLTK:")
print(stop_words)
# --> the stop words are all lower case
print(len(stop_words))

# Split example sentence into words
word_list_example=word_tokenize(example_sentence.lower())
# Create list for filtered words
word_list_filtered=[]

# filter out stop words
for word in word_list_example:
    if word not in stop_words:
        word_list_filtered.append(word)

print("Example sentence after stop words have been deleted:")
print(word_list_filtered)

# How does the example from above look like?
test_text_filtered=[]

# filter out stop words
for word in word_tokenize(test_text.lower()):
    if word not in stop_words:
        test_text_filtered.append(word)

print("Test text after stop words have been deleted:")
print(test_text_filtered)


################
# 3. Stemming
################
# define an abbreviation
ps=PorterStemmer()

example_words_1=["play", "player", "players", "played", "playing"]

for word in example_words_1:
    print(ps.stem(word))
    # the full syntax without the abbreviation would be:
    print(PorterStemmer().stem(word))

# adjectives and adverbs
example_words_2=["high", "higher", "highest", "highly", "height"]
for word in example_words_2:
    print(ps.stem(word))
# --> comparative and superlative are not reduced to the stem/regular adjective
# neither are adverbs

# Let's see how the stemmer deals with irregular words.
example_words_3=["good", "better", "best", "well", "God", "Goodness"]
for word in example_words_3:
    print(ps.stem(word))
# --> upper case words are also transformed to lower case.

# Stem the test text from above
# Approach 1: stem word by word
test_text_stemmed=[]
for word in word_tokenize(test_text):
    test_text_stemmed.append(ps.stem(word))

print("Stemming word by word: test text after it has been stemmed:")
print(test_text_stemmed)

# Alternative approach: stem entire text
test_text_stemmed=ps.stem(test_text)
print("Stemming entire document: test text after it has been stemmed:")
print(test_text_stemmed)
# -> does not work

print("End of nltk introduction!")
