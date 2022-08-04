# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 21:56:41 2017

@author: Alexander Hillert, Goethe University Frankfurt
"""

import nltk
import random
import collections
import re

# We will use the NLTK Corpus containing 2,000 Movie Reviews of which 1,000
# are positive and the other 1,000 are negative.
# if you do not have the movie review corpus yet, download it:
nltk.download("movie_reviews")

from nltk.corpus import movie_reviews


# Create a list that contains the tuples of document and category.
# Category is "positive" or "negative"
documents = []
# For all categories
for category in movie_reviews.categories():
    print("Category: "+str(category))
    # for all reviews (identified by file ID) in the respective category
    for file_ID in movie_reviews.fileids(category):
        # You have to put two parentheses to indicate that you want to add a tuple.
        documents.append((list(movie_reviews.words(file_ID)),category))

# Print the first element (i.e. tuple) of documents.
print(documents[0])
# print the words of the first movie review
print(documents[0][0])
# print the first word of the first movie review
print(documents[0][0][0])

# print the classification of the first movie review
print(documents[0][1])

# print the classification of the 1000th review (the last negative one)
print(documents[999][1])
# print the classification of the 1001st review (the first positive one)
print(documents[1000][1])

# The default order of the reviews is first all negative reviews and then all positive ones.
# Later we will build a training and a testing set. As we need to have positive and negative
# reports in both sets, we randomly shuffle the documents.
random.shuffle(documents)

# Create a list of all words.
all_words = []
for word in movie_reviews.words():
    # We use lower case words
    #all_words.append(word.lower())
    if re.search("\A[a-z]",word.lower()):
    # check whether the word is actually a word, i.e., whether it contains
    # at least one letter
    #if re.search("[a-z]",word.lower()):
        # We use lower case words
        all_words.append(word.lower())
    

# What are the most frequently used words in the movie reviews?
# Alternative 1:
# FreqDist sort words from the most frequently used word to the least frequenty used word.
all_words_approach_1 = nltk.FreqDist(all_words)
print("Alternative 1: the top 15 words are: "+str(all_words_approach_1.most_common(15)))

# Alternative 2:
# We can also determine the most frequent words by using Counters as we did
# in Problem 12 --> transform list of all words to a Counter
all_words_approach_2=collections.Counter(all_words)
top_15_words=all_words_approach_2.most_common(15)
print("Alternative 2: the top 15 words are: "+str(top_15_words))
# -> identical results -> perfect.

# Search for a word and see how often it appears.
print("The word 'stupid' appears "+str(all_words_approach_1["stupid"])+" in the movie reviews.")
# alternatively
print("The word 'stupid' appears "+str(all_words_approach_2["stupid"])+" in the movie reviews.")

# How can we restrict the set of words that we use for training the Naive Bayes algorithm?
# -> create a list that only contains the top 3000 words
# get the top 3000 words
# Approach 1 using the NLKT.FreqDist from above
i=0
top_3000_words=all_words_approach_1.most_common(3000)
list_top_3000_words_approach_1=[]
while i<3000:
    list_top_3000_words_approach_1.append(top_3000_words[i][0])
    i=i+1
    
# Approach 2 using Counters from above
i=0
top_3000_words=all_words_approach_2.most_common(3000)
list_top_3000_words_approach_2=[]
while i<3000:
    list_top_3000_words_approach_2.append(top_3000_words[i][0])
    i=i+1

# select the list of approach 1 or 2
word_features=list_top_3000_words_approach_1

# We need to identify the words we want to use for classification in the documents.
# We define a function for that.
def find_features(document):
    words = set(document)
    features = {}
    # loop over all the words we consider for the classification
    for word in word_features:
        # The expression returns either true or false
        features[word] = (word in words)
    
    return features

# To get an idea what the function find_features() does let's print the features
# for one review.
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))


feature_set = [(find_features(review), category) for (review, category) in documents]

# How does feature set looks like?
print(feature_set[0])
# -> it is still a tuple
print(feature_set[0][0])
# the first element are the 3000 words we use for classification with "True" or "False"
# depending on whether the words appear in the review
print(feature_set[0][1])
# Is the information on whether the review is positive or negative

# Define the training and testing set
# The training set comprises the first 1900 reviews and the testing set the last 100 reviews.
training_set=feature_set[:1900]
testing_set=feature_set[1900:]

# First we have to train the Naive Bayes Classifier.
# It will determine which of the words from word_features appear mostly in positive
# reviews and which appear mostly in negative reviews.
classifier=nltk.NaiveBayesClassifier.train(training_set)
# The following command prints the 20 words that best discriminate between
# positive and negative reviews.
classifier.show_most_informative_features(20)

# Let's classify the first element of feature_set
# The input for the classification need to be the list of words with True or False
print(classifier.classify(feature_set[0][0]))
print("The review is actually: "+str(feature_set[0][1]))

# classify the 100 reports from the testing set
# they have the position 1900 to 2000 in the feature set.
i=1900
classified_set=[]
while i<2000:
    classified_set.append(classifier.classify(feature_set[i][0]))
    i=i+1

# Compare classification result with actual category
i=0
# In this list we save tuples of [predicted category, actual category]
comparison=[]
# In this list we simply save "accurate" and "inaccurate"
comparison_2=[]
while i<100:
    comparison.append([classified_set[i],feature_set[i+1900][1]])
    # If the predicted and acutal classification match -> accurate
    if comparison[i][0]==comparison[i][1]:
        comparison_2.append("accurate")
    else:
        comparison_2.append("inaccurate")
    i=i+1

print(comparison)
# We need the number of accurate and inaccurate classifications
comparison_counter=collections.Counter(comparison_2)
print(comparison_counter)

# NLT can compute the accuracy directly
# What is the accuracy for the testing set?
print("Naive Bayes accuracy (in percent):", (nltk.classify.accuracy(classifier, testing_set))*100)
# Same value as from our own calculations -> perfect!

# What is the accuracy for the training set?
print("Naive Bayes accuracy in training data (in percent):", (nltk.classify.accuracy(classifier, training_set))*100)
# Higher than in the testing dataset -> expected.

print("completed!")
