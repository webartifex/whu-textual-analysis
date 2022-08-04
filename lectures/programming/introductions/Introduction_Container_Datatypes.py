# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:19:54 2017

@author: Alexander Hillert, Goethe University Frankfurt
This version: February 22, 2019

This is an introduction to two data containers: lists and counters.

Python has several built-in data containers, e.g., sets, dictionaries, and lists
In addition to these containers, there are further types.
For textual analysis application counters are helpful.

This introduction covers lists in the first part.
The second part introduces the basics of counters.
"""

# for counters, you need to import collections
import collections
import re

###############################################################################
# Introduction on data containers
###############################################################################

#################################
# Part 1: lists
#################################
# Create an empty list
empty_list=[]

# Create non-empty lists
string_list=["a", "b", "c"]
mixed_list=[1, "ab", -4,"hello"]

print(mixed_list)

# Call items of a list
print(string_list[0])
print(string_list[2])
print(string_list[-1])

# Length of a list
length=len(string_list)
print("The length of the list is: "+str(length))


# ADD ITEMS TO A LIST
# ALTERNATIVE 1: insert -> you can specify the position
string_list.insert(1,"d")
# you cannot add multiple elements with the insert command
# You can try, but it will not work
# 1st try
string_list.insert(3,"e" "f") # -> the new element is "ef"
print(string_list)
# 2nd try
try:
    string_list.insert(3,"e", "f")
except:
    print("Wrong syntax. If the command were executed without the try-except "\
    "you would get the error TypeError: insert() takes exactly 2 arguments (3 given)'")
# 3rd try
string_list.insert(3, ["e", "f"])
# check length
print("The length of the list is: "+str(len(string_list))) # -> only 6 and not 7
print(string_list[3])
# So element 3 of the list is another list
# You can call the elements of the sub-list
print("First element of sub list: "+string_list[3][0]+" and second element of \
      sub list: "+string_list[3][1])

# Reset string_list to keep things easily tractable
string_list=["a", "b", "c"]

# ALTERNATIVE 2: append -> items are added at the end
string_list.append("d")

# Try to add multiple items
# 1st try
string_list.append("e" "f") # -> the new element is "ef"
print(string_list)
# 2nd try
try:
    string_list.append("e", "f")
except:
    print("Wrong syntax. If the command were executed without the try-except "\
    "you would get the error 'TypeError: append() takes exactly one argument (2 given)'")
# 3rd try
string_list.append(["e", "f"])
# check length
print("length of list is "+str(len(string_list))) # -> only 6 and not 7
print(string_list[len(string_list)-1])
# -> element 3 of the list is another list
# You can call the elements of the sub-list
print("First element of sub list: "+string_list[len(string_list)-1][0]+" and \
        second element of sub list: "+string_list[len(string_list)-1][1])

# Reset string_list to keep things easily tractable
string_list=["a", "b", "c"]

# ALTERNATIVE 3: extend -> items are added at the end
string_list.extend("d")

# Try to add multiple items
# 1st try
string_list.extend("e" "f") # -> Two elements are created -> works!!!
print(string_list)
# 2nd try
try:
    string_list.extend("e", "f")
except:
    print("Wrong syntax. If the command were executed without the try-except "\
    "you would get the error 'TypeError: extend() takes exactly one argument (2 given)'")
# 3rd try
string_list.extend(["e", "f"])
print(string_list) # -> also works!!!
# check length
print("length of list is "+str(len(string_list))) # -> it is 8 and should be 8


# DELETE ITEMS FROM A LIST
string_list.remove("a")
print("List after deletion of 'a' "+str(string_list))
# What happens if an element occurs multiple times
string_list.remove("e")
print("List after further deletion of 'e' "+str(string_list))
# --> only first occurence of "e" is deleted


# FURTHER OPERATIONS WITH LISTS
# Accessing parts of a list
# Remember the first element is [0]! And the upper bound of the range is not
# included, i.e. [0:3] means [0], [1] and [2].
print("Sublist from beginning to third element: "+str(string_list[0:3]))
print("Sublist from beginning to third element: "+str(string_list[:3]))
print("Sublist from second(!) to third element: "+str(string_list[1:3]))
print("Sublist from fourth(!) to fifth element: "+str(string_list[3:5]))
print("Sublist from fifth(!) to the end: "+str(string_list[4:]))

# Search in lists
position=string_list.index("b")
print("Position of 'b' is: "+str(position))
# Searching for an element that is not part of the list
try:
    string_list.index("a")
except:
    print("Error message. If the command were executed without the try-except "\
    "you would get the error 'ValueError: 'a' is not in list'")
if "c" in string_list:
    print("'c' is at position: "+str(string_list.index("c")))
    
# Sort list
string_list.sort()
print('Sorted list: '+str(string_list))
string_list.sort(reverse=True)
print('Reversely sorted list: '+str(string_list))

# What happens when sorting mixed (i.e. integers and strings) lists?
try:
    mixed_list.sort()
except:
    print("Error message. If the command were executed without the try-except "\
    "you would get the error 'TypeError: unorderable types: str() < int()'")


#################################
# Part 2: counters
#################################
'''
A Counter is a dictionary subclass for counting hashable objects.
It is an unordered collection where elements are stored as dictionary keys and
their counts are stored as dictionary values.
'''
# Creating a counter
counter_obj=collections.Counter(["a", "b", "c", "d", "a", "b", "a"])
print('The counter object is: '+str(counter_obj))
# The previous command is equivalent to
counter_obj=collections.Counter(a=3, b=2, c=1, d=1)
print('The counter object (2nd command) is: '+str(counter_obj))

# Add objects to a counter
counter_obj.update(["e", "f", "e"])
print('The updated counter object is: '+str(counter_obj))
# Alternative command
counter_obj["g"]=4
print('The updated updated counter object is: '+str(counter_obj))

# Length of the counter
length=len(counter_obj)
print('The length of the counter is: '+str(length))

# Loop over the elements of the counter and their frequency
i=1
for element in counter_obj:
    print("Element "+str(i)+" of the counter: "+str(element))
    print("Frequency of Element "+str(i)+" of the counter: "+str(counter_obj[element]))
    i=i+1

# .elements() provides an iterator of all individual elements of the counter
counter_elements=list(counter_obj.elements())
print('Elements of the counter: '+str(counter_elements))

# APPLY COUNTERS TO TEXTS
sentence1="This is the first sentence."
sentence2="This is the second sentence, which is longer."

# Split sentences in words
sentence1_words=re.split("\W{1,}", sentence1)
print("The last element is: "+str(sentence1_words[len(sentence1_words)-1]))
# The last element is empty -> delete it.
sentence1_words.remove("")
print("The last element is: "+str(sentence1_words[len(sentence1_words)-1]))
# -> now okay
sentence2_words=re.split("\W{1,}", sentence2)
print("The last element is: "+str(sentence2_words[len(sentence2_words)-1]))
# The last element is empty -> delete it.
sentence2_words.remove("")
print("The last element is: "+str(sentence2_words[len(sentence2_words)-1]))
# -> now okay

# Counter words
sentence1_counter=collections.Counter(sentence1_words)
sentence2_counter=collections.Counter(sentence2_words)

print(sentence1_counter)
print(sentence2_counter)

# OPERATIONS WITH COUNTERS
# add counters
add_counters=sentence1_counter+sentence2_counter
print("You can add counters: "+str(add_counters))

# subtract counters
subtract_counters=sentence1_counter-sentence2_counter
print("You can subtract counters: "+str(subtract_counters))
# Each time a new Counter is produced through an operation, any items with zero
# or negative counts are discarded. --> only first appears in subtract_counters

# Intersection of counters
intersection_counters=sentence1_counter & sentence2_counter
print("You can determine the intersection of counters: "+str(intersection_counters))
# -> takes the minimum of occurences; again elements with zero frequency
# are not included.

# Union of counters
union_counters=sentence1_counter | sentence2_counter
print("You can determine the union of counters: "+str(union_counters))
# -> takes the maximum of occurences

# MOST FREQUENT WORDS
# Determine the three most frequent words in the add_counters set.
top_3_words=add_counters.most_common(3)
print("The top 3 words are: "+str(top_3_words))

# Identify the two most frequent words with the top 4 words in the add_counters sample.
top_4_words=add_counters.most_common(4)
# The first [] refers to the line, i.e. is it the second common, second most
# frequent word.
# The second[] refers either to the word itself [0] or to the frequency of the word [1].
# the most frequent word
top_word=top_4_words[0][0]
top_word_count=top_4_words[0][1]
print("The top word is '"+str(top_word)+"', which appears "+str(top_word_count)+" times")
# the second most frequent word
top_2_word=top_4_words[1][0]
top_2_word_count=top_4_words[1][1]
print("The second most frequent word is '"+str(top_2_word)+"', which appears "+str(top_2_word_count)+" times")


print("Completed")
