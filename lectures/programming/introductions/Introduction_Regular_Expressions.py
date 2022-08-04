# -*- coding: utf-8 -*-
"""
INTRODUCTION TO REGULAR EXPRESSION

@author: Alexander Hillert, Goethe University Frankfurt
This version: June 3, 2019

What are regular expressions?

Regular expressions allow you to search for general patterns in texts. The
standard string commands like .count("search_term") and .replace("old_word","new_word") 
can only count and replace one specific word, respectively. They cannot search
for general patterns like all words that consist of three or more letters.
Assume that you want to identify all numbers in a text or that you search for
the year of birth in bios of corporate executives. In the examples, you need a
search tool that can process broad patterns --> you need regular expressions.
Consider the second example, i.e. you would like to automatically identify
people's year of birth from their bios. You know that the number must have four
digits and that the first two digits must equal 19. Of course, you could 
hardcode all possible years (1900, 1901, ..., 1999), but this is unnecessarily
complicated and slows down the program. Therefore, it is better to learn 
how to use regex.

Useful online resources:
1. https://regex101.com/
On this webpage, you can enter a text and a regular expression.
The webpage highlights the matches and provides explanations for
every part of the regex pattern.
Caution: click on "Python" in the left menu (the default language is php)!

2. https://docs.python.org/3/library/re.html
The offical documentation of regular expression in Python 3.

"""

# To be able to use regular expressions you need to import the re package first.
import re

# Select the directory where you saved the accompanying txt-file.
directory="C:/Lehre/Textual Analysis/Programming/Files/"


# In this introduction, we use the accompanying txt-file "Text_Introduction_Regular_Expressions.txt"
# open the file
text_file=open(directory+'Text_Introduction_Regular_Expressions.txt','r',encoding='cp1252')
# read its content
text=text_file.read()

# Let's start with the example from the beginning and search for people's years of birth.
# The standard search command for regular expressions is re.search. It searches
# for the FIRST match of the expression in the text.
# First try
match=re.search("19[0-9]{2}",text)
# This command searches for four digits of which the first is a 1, the second a 9,
# and then there are two further digits which can be any digits.
# [0-9] refers to any digit. Equivalently, you can write \d which also refers
# to any digits.
# The {2} specifies that there must be exactly to digits.

print(match)
# match contains information on the match:
# span is the position in text where the match starts and ends; here 226 and 230
# furthermore, the matched text is shown. Here, the first match is 1956.
# You can use the positions to print the text before the match, after the match,
# and, of course, of the matched text.
start=match.start()
end=match.end()
print("From beginning of the document to the match: \n"+text[:start]+"\n\n")
print("The match itself: \n"+text[start:end]+"\n\n")
print("From end of match to end of document: \n"+text[end:]+"\n\n")

# To access the match, you can also use the command .group(0):
print("Alternative way to access the matched text: \n"+match.group(0)+"\n\n")

# CAUTION
# If no match is found the variable match does not exist.
# Example: search for a ten digit number that start with 19
match=re.search("19[0-9]{8}",text)
# The command start=match.start() returns the follwoing error:
# "AttributeError: 'NoneType' object has no attribute 'start'"
# SOLUTION
match=re.search("19[0-9]{8}",text)
if match:
    # match found, the start .start() is now conditional on the existence of match
    start=match.start()
    print("Match found. Starting at position "+str(start))
else:
    # no match found
    print("No match found")

'''
Information on Syntax, Special Characters in Regular Expression

Character       Meaning
[]              Indicates a set of characters
\[              Matches the actual [
\]              Matches the actual ]
^               negation; the symbols listed afterwards are not allowed in the match
                E.g., [^0-9] will not match any numbers but all other symbols.
\d              Any digit, i.e. 0, 1, 2, ..., 9. Equivalent to [0-9]
\n              Linefeed/newline, the start of a new line.
\s              Any whitespace, i.e. a tab, a space.
                CAUTION: \s matches also the newline (\n). This property of \s
                can lead to unintended matches.
                RECOMMENDATION: to match whitespaces only use [ \t], i.e. a space
                and a tab (\t).
\S              Any non-whitespace symbol.
.               Any character (digit, letter, symbol [!,?,%,etc.], spaces) but
                NOT the newline, \n.
\.              Matches the actual dot.
\w              Matches word characters, i.e. [0-9a-zA-Z_]
                The underscore (_) is defined to be a word character.
\W              Matches any non-word characters, i.e. [^0-9a-zA-Z_]
|               Or condition (for an example see line 272)
()              Like in math: parentheses indicate which characters of an expression 
                belong togehter. (For an example see line 272.)
\(              Matches the actual (
\)              Matches the actual )

(?i)            Performs the regex case-insensitive. Must be put at the beginning
                of the regex. E.g. re.search("(?i)TeSt",text) will match
                TEST, test, Test, etc.
re.IGNORECASE   Performs the regex case-insensitive. Must be put at the end of
                the regex as an option. E.g. re.search("test",text,re.IGNORECASE)
'''
# Examples of character sets
# 1. [0-9]: numbers
match=re.search("[0-9]","ABC abc 123")
print(match)
#2. [a-z]: any lower case letter
match=re.search("[a-z]","ABC abc 123")
print(match)
#3. [A-Z]: any upper case letter
match=re.search("[A-Z]","ABC abc 123")
print(match)
#4. [cde]: lower case letters c, d, and e.
match=re.search("[cde]","ABC abc 123")
print(match)
#5. [^A-Zab]: all symbols except captial letters and a and b.
match=re.search("[^A-Zab]","ABC abc 123")
print(match)
# you don't see any character because the match is the first white space before abc


'''
Quantifiers for regular expression:
n and m refer to non-negative integers (0, 1, 2, ...), where m>n
Quantifier      Meaning
{n}             The preceding pattern must be found EXACTLY n times.
{n,}            The preceding pattern must be found AT LEAST n times.
{,n}            The preceding pattern must be found AT MOST n times.
{n,m}           The preceding pattern must be found AT LEAST n but AT MOST m times.
{n,}?           The ? tells the regex not to be "greedy" (see lines 211 for details)

There are alternative notations for commonly used quantifiers:
* is equivalent to {0,}, i.e. 0 or more repetitions of the preceding pattern.
+ is equivalent to {1,}, i.e. 1 or more repetitions of the preceding pattern.
? is equivalent to {0,1}, i.e. 0 or 1 repetition of the preceding pattern.
'''

# re.search() returns only the first match: How to get all matches?
# Alternative 1: use a loop.
text1=text
i=1
match=re.search("19[0-9]{2}",text1)
# Repeat the following commands until no more matches are found.
while match:
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    end=match.end()
    text1=text1[end:]
    match=re.search("19[0-9]{2}",text1)
    i=i+1

# Alternative 2: use re.findall
# The syntax is identical to re.search
list_of_matches=re.findall("19[0-9]{2}",text)
print(list_of_matches)
# the individual matches can be called by list_of_matches[i], where i ranges
# from zero to the number of matches minus one.
# Remember: the first element of a list has the position 0
for i in range(0,len(list_of_matches)):
    print("This is match number "+str(i+1)+" using the re.findall command: "+list_of_matches[i])


# When you read the text you will observe that there are only six years of birth
# in the text and not eight -> there are two mismatches -> adjust filter to 
# get only the years of birth and not all years.
text1=text
i=1
# Check whether the word born appears before the year. The distance between
# born and the year must be smaller or equal 15 (plus the two white spaces)
match=re.search("born .{,15} 19[0-9]{2}",text1)
while match:
    print("This is match number "+str(i)+": "+match.group(0))
    # Extract the year
    match1=re.search("19[0-9]{2}",match.group(0))
    print("The year of match number "+str(i)+" is: "+match1.group(0))
    # Check whether there are further matches after the end of the previous match
    end=match.end()
    text1=text1[end:]
    match=re.search("born .{,15} 19[0-9]{2}",text1)
    i=i+1
 

# The quantifiers introduced above are "greedy". For example, if a pattern matches overlapping
# text parts of different length, the regex will return the longest match.
# Example: search for the first sentence in a text. You know that sentences
# end with period in this example.
text2="This is the first senctence. This is the second sentence. And so on"
# Search for a positive number of occurances of characters followed by a period.
# Remeber that the dot is \. in regex. The . will match any character.
match=re.search(".{1,}\.",text2)
print(match.group(0))
# -> the regex returns the first and second sentence.
# To get the first match that fulfils the regex, put a ? after the quantifiers.
# This makes the quantifier "non-greedy", and only the first occurance will be matched.
match=re.search(".{1,}?\.",text2)
print(match.group(0))

# You will often have situations where there are multiple versions of the same
# pattern. How can you include all of them in one regular expression?
# Example 1: search for the word "losses" in the following sentence:
text3="X Corp's soda division returned significant losses in the last quarter. Losses will be reduced this quarter."
# the first letter of "loss" can be upper or lower case
print("Example 1: Loss and loss")
text4=text3
i=1
# A set of characters [] is matched if at least one of the components of the
# set is found in the text. This works only for a single letter/number/symbol
# but not for sequences of multiple letters/numbers/symbols.
match=re.search("[Ll]oss",text3)
while match:
    end=match.end()
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    text4=text4[end:]
    match=re.search("[Ll]oss",text4)
    i=i+1

# Alternatively
list_of_matches=re.findall("[Ll]oss",text3)
print("Alternative using re.findall: "+str(list_of_matches))

# In this example, you could also simply perform a case-insensitive match.
print("Case-INsensitive matching using re.IGNORECASE")
text4=text3
i=1
match=re.search("loss",text3,re.IGNORECASE)
while match:
    end=match.end()
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    text4=text4[end:]
    match=re.search("loss",text4,re.IGNORECASE)
    i=i+1
# Or equivalently
print("Case-INsensitive matching using (?i)")
text4=text3
i=1
match=re.search("(?i)loss",text3)
while match:
    end=match.end()
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    text4=text4[end:]
    match=re.search("(?i)loss",text4)
    i=i+1


# Example 2: search for the expressions "profits declined" and "profits decreased"
# in the following sentence:
text3="X Corp's profits declined in 2010, while Y Inc.'s profits decreased the year before."
# Here, [] no longer works because we need to match terms consisting of several
# characters and [] matches only one character. -> use the OR-operator |
print("Example 2: profits declied and profits decreased - First try")
text4=text3
i=1
match=re.search("profits declined|decreased",text3)
while match:
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    end=match.end()
    text4=text4[end:]
    match=re.search("profits declined|decreased",text4)
    i=i+1
# Problem: regex interprets the entire set of characters before the | as one
# alternative.
# Solution: use parantheses to define the boundaries.

print("Example 2: profits declied and profits decreased - Second try")
text4=text3
i=1
match=re.search("profits (declined|decreased)",text3)
while match:
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    end=match.end()
    text4=text4[end:]
    match=re.search("profits (declined|decreased)",text4)
    i=i+1

# Alternative: does re.findall work?
list_of_matches=re.findall("profits (declined|decreased)",text3)
print(list_of_matches)
# -> No! Because there is a major difference between re.search and re.findall
# in the way they treat parantheses ().
# re.search follows the general regular expression syntax that is also used in
# other programming languages.
# To use re.findall you have to write down the full text before and after the |.
list_of_matches=re.findall("profits declined|profits decreased",text3)
print(list_of_matches)


# More information on the difference between re.search and re.findall
# Example 3: let's search for the numbers in the second part of the txt file
# and compare what the two commands do.
# Get the second part
match=re.search("Here are some numbers:",text)
text4=text[match.end():]
print(text4)
match=re.search("[0-9]{1,}([0-9]{3}|,){0,}\.{0,1}[0-9]{0,}",text4)
# What are the individual parts of this pattern?
# [0-9]{1,} There has to be at least one digit.
# ([0-9]{3}|,){0,} The first digit can be followed by combinations of three
# digits and commas (as thousand separator).
# \.{0,1} There can be zero or one period as decimal separator.
# [0-9]{0,} There can be multiple decimal places.

i=1
while match:
    print("This is match number "+str(i)+": "+match.group(0))
    # Check whether there are further matches after the end of the previous match
    end=match.end()
    text4=text4[end:]
    match=re.search("[0-9]{1,}([0-9]{3}|,){0,}\.{0,1}[0-9]{0,}",text4)
    i=i+1

# Can we obtain the same result by using re.findall?
match=re.search("Here are some numbers:",text)
text4=text[match.end():]
list_of_matches=re.findall("[0-9]{1,}([0-9]{3}|,){0,}\.{0,1}[0-9]{0,}",text4)
print(list_of_matches)
# Does not work!
# One has to put "?:" in the part that captures the repetition of the thousands.
# This tells re.findall to return the full match and not subpatterns.
list_of_matches=re.findall("[0-9]{1,}(?:[0-9]{3}|,){0,}\.{0,1}[0-9]{0,}",text4)
print(list_of_matches)

# TAKE AWAY: The matching of re.findall does not always match that of re.search
# Be careful when using re.findall!!!


# How to delete or substitute parts of texts?
# Alternative 1: identify the beginning and end of the matched text part and
# remove it from the overall text.
# Example delete all numbers in the text
text4=text
print("Original Text:\n"+text4)
match=re.search("[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}",text4)
while match:
    # Remove the match
    text4=text4[:match.start()]+text4[match.end():]
    # Check whether there are further matches in the remaining text
    match=re.search("[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}",text4)
print("Text without numbers using re.search:\n"+text4)

# Alternative 2: use re.sub (sub -> substitute)
# syntax: new_text=re.sub(pattern, replacement, old_text)
# replacement is some string. Regular expressions are only allowed in the pattern
# but not in the replacement.
text4=text
text4=re.sub("[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}","",text4)

print("Text without numbers using re.sub:\n"+text4)
# re.sub is the more efficient way.
# Furthermore, re.sub can not only delete text but also replace text.
# Example
text4=text
text4=re.sub("[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}","NUMBER",text4)
print("Text where numbers are replaced by the word 'NUMBER':\n"+text4)


# Make sure you get the right match --> importance of word boundaries.
# When you search for a word it can happen that the word is part of a different
# longer word. For example, searching for "high" would also match "highlight".
# To avoid such mismatches you can either include word boundaries in the search
# (Alternative 1) or split the text first by word boundaries into single words
# and perform standard string search operations afterwards (Alternative 2).
# Alternative 2 does not return the individual matches but tells you for example
# the number of matches
# Example: search for the word "is"
# Alternative 1:
match=re.search("is",text)
print("Searching without word boundaries yields: '"+match.group(0)+\
"' But the surrounding text is: '"+text[match.start()-1:match.end()+1]+"'")
match=re.search("\Wis\W",text)
print("Searching with word boundaries yields: '"+match.group(0)+\
"' and the surrounding text is: '"+text[match.start()-1:match.end()+1]+"'")
# You see that the preceding and subsequent word boundaries are also matched
# and saved as the matched term. However, often you want the match to include only
# the actual word without its boundaries.
# Solution: use so called "look ahead" and "look back" conditions.

'''
Look ahead and look behind/back conditions

Regex requires that the parts of the pattern that are classified as look ahead
or look back/behind are present in the text but does not include them in the match.

Syntax:
positive look ahead:    (?=)      Example: X(?=\W) requires that there is a word
                                           boundary after X
negative look ahead:    (?!)      Example: X(?!\W) requires that there must NOT
                                           be a word boundary after X.                                         
positive look back:    (?<=)      Example: (?<=\W)X requires that there is a word
                                           boundary before X
negative look back:    (?<!)      Example: (?<!\W)X requires that there must NOT
                                           be a word boundary before X.
'''
match=re.search("(?<=\W)is(?=\W)",text)
print("Searching with word boundaries as look ahead and look back condition yields: '" #
      +match.group(0)+"' and the surrounding text is: '"+text[match.start()-1:match.end()+1]+"'")

# Does it work also with re.finall?
list_of_matches=re.findall("\Wis\W",text)
print("Word boundaries using re.findall: "+str(list_of_matches))
list_of_matches=re.findall("(?<=\W)is(?=\W)",text)
print("Word boundaries as look ahead and look back condition using re.findall: "+str(list_of_matches))
print("In total there are "+str(len(list_of_matches))+" matches.")
# --> Yes, the approach also work with re.findall.

# Alternative 2:
# Use re.split(), which is similar to split() but more powerful.
text_split=re.split("\W",text)
print(text_split)
# Problem: there are elements in the list that are not words, e.g. ''. These
# elements are created because there can be a series of non-word characters (\W),
# e.g. ' (' in 'Balmer (born'.
# Solution: treat a series of wordboundaries \W as a single split character
text_split=re.split("\W{1,}",text)
print(text_split)
# Now, you do not need to include word boundaries and can use standard string
# operations.
number_matches=text_split.count("is")
print("Using standard string operations, we get "+str(number_matches)+" matches.")
# -> same result.
