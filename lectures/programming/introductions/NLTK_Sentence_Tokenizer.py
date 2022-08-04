# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:09:50 2021

@author: ahillert
"""

from nltk.tokenize import sent_tokenize

print("\nExample 1\n")
text_1="The S&P 500 rose 43.44 points to 4,159.12. The Dow Jones industrial average " \
+"added 188.11 points, or 0.6 percent, to 34,084.15. The tech-heavy Nasdaq fared " \
+"better than the rest of the market, climbing 236 points, or 1.8 percent, to 13,535.74"

sentence_list_1=sent_tokenize(text_1)

for i in range(0,len(sentence_list_1)):
    print("This is sentence "+str(i+1)+":\n"+sentence_list_1[i])

# -> good performance

print("\nExample 2\n")
text_2=text_1.lower()

sentence_list_2=sent_tokenize(text_2)

for i in range(0,len(sentence_list_2)):
    print("This is sentence "+str(i+1)+":\n"+sentence_list_2[i])

# -> poor performance
# For the NLTK tokenizer it makes a difference whether text is lower or upper case.


print("\nExample 3\n")
text_3="On Sept. 16, 2020, the U.S. president appointed John D. Smith as head of the F. B. I. " \
+"While Jane C. Taylor became the president of the S. E. C. " \
+"On Jan. 5, 2020, J. C. Penny filed for bankruptcy. Michael T. Brown - reporting from Washington D.C."

sentence_list_3=sent_tokenize(text_3)

for i in range(0,len(sentence_list_3)):
    print("This is sentence "+str(i+1)+":\n"+sentence_list_3[i])

# -> good performance

print("\nExample 4\n")
text_4=text_3.lower()

sentence_list_4=sent_tokenize(text_4)

for i in range(0,len(sentence_list_4)):
    print("This is sentence "+str(i+1)+":\n"+sentence_list_4[i])