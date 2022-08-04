# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe University Frankfurt
"""

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter


ps=PorterStemmer()

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 10-Ks from MSFT, KO, and 3M
input_file=open(directory+'list_10-K_filings_textual_similarity.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the input file in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the iput file. The following command
# deletes these lines
while input_text_line.count("")>0:
    input_text_line.remove("")

# Open the output csv file in which we write the similarities
output_file=open(directory+'list_10-K_filings_textual_similarity_jaccard.csv','w',encoding="utf-8")
# Write variable names to first line
output_file.write(input_text_line[0]+';Jaccard;Jaccard_own_stop_words;\
Jaccard_NLTK_stop_words;Jaccard_stemmed;Jaccard_stemmed_own_stop_words;\
Jaccard_stemmed_NLTK_stop_words\n')

# Read own stop word list
# This list has been created by manually selecting words from the csv-file
# 100_most_frequent_words.csv, which is created by the Python program
# "Problem_12_Most_Frequent_Words.py".
# Simply delete words you consider to be meaningless and that are frequently
# used.
stop_word_file=open(directory+'Stop_Word_List_Alexander.csv','r',encoding="utf-8")
stop_word_text=stop_word_file.read()
stop_word_line=stop_word_text.split("\n")
stop_word_line.remove("")
own_stop_words=[""]
for i in range(1,len(stop_word_line)):
    stop_word=stop_word_line[i].split(";")[1]
    own_stop_words.append(stop_word)

own_stop_words.remove("")
print("This is the list of my stop words:")
print(own_stop_words)

# Read NLTK stop word list
NLTK_stop_words=set(stopwords.words("english"))
print("This is the list of NLTK stop words:")
print(NLTK_stop_words)

# set default values for variables
# It is not required. However, if you don't do it Spyder will suggest that line
# jaccard_similarity=jaccard(word_list_edited,word_list_old_edited)
# is incorrect as word_list_old_edited is not yet defined at point in the program
# code. In this specific example, this will not cause an error, as we do not enter
# the if condition when i=1 -> it
word_list_old_edited=[]
word_list_edited=[]
word_list_old_NLTK_filtered=""
word_list_old_own_filtered=""
word_list_old_edited_stemmed=""
word_list_old_own_filtered_stemmed=""
word_list_old_NLTK_filtered_stemmed=""

#######################################################
# Define a function that computes Jaccard similarity
# As we need these operations several times, it is
# helpful to use a function.
######################################################
# beginning of the function
def jaccard(text1,text2):
    counter1=Counter(text1)
    counter2=Counter(text2)

    intersection=counter1 & counter2
    union=counter1 | counter2

    return len(intersection)/len(union)
# end of the function


# Loop over all lines
for i in range(1,len(input_text_line)):
    print(str(i))
    # split the line into the eight variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (8th column)
    cik=variables[0]
    filename_parts=re.split('/',variables[7])
    filename=filename_parts[3].replace('.txt','')
    
    # Write the information from the input file to the output file
    # we do not add a line break at the end, as we must append the similarity
    # score first.
    output_file.write(input_text_line[i])
    
    # Open the ith 10-K; remember to specify the encoding
    input_file_10_k=open(directory+'10-K_Textual_Similarity/'+cik+'_'+filename+\
    '_edited.txt', 'r', encoding='ascii', errors='ignore')
    input_text_10_k=input_file_10_k.read()
    
    # check whether the previous entry of the list is from the same firm
    permco=input_text_line[i].split(";")[1]
    permco_old=input_text_line[i-1].split(";")[1]
    
    # Split text into words
    word_list_edited=word_tokenize(input_text_10_k.lower())
    
    
    ############################################
    # Sub Task 1: Jaccard for the _edited.txt
    ############################################
    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        # the command calls the jaccard function that we have defined above.
        # in the function, text1=word_list_edited and text2=word_list_old_edited.
        jaccard_similarity=jaccard(word_list_edited,word_list_old_edited)
         
        output_file.write(";"+str(jaccard_similarity))
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(";")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_edited=word_list_edited
    
    
    ############################################
    # Sub Task 2: Jaccard for the _edited.txt
    # AND REMOVE STOP WORDS - OWN LIST
    ############################################
    # remove stop words using personal stop word list
    word_list_own_filtered=[]
    for word in word_list_edited:
        if word not in own_stop_words:
            word_list_own_filtered.append(word)

    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        jaccard_similarity=jaccard(word_list_own_filtered,\
        word_list_old_own_filtered)
         
        output_file.write(";"+str(jaccard_similarity))
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(";")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_own_filtered=word_list_own_filtered
    
    
    ############################################
    # Sub Task 3: Jaccard for the _edited_v1.txt
    # AND REMOVE STOP WORDS - NLTK LIST
    ############################################
    # remove stop words using NLTK stop word list
    word_list_NLTK_filtered=[]
    for word in word_list_edited:
        if word not in NLTK_stop_words:
            word_list_NLTK_filtered.append(word)

    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        jaccard_similarity=jaccard(word_list_NLTK_filtered,\
        word_list_old_NLTK_filtered)
        
        output_file.write(";"+str(jaccard_similarity))
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(";")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_NLTK_filtered=word_list_NLTK_filtered
    
    
    ############################################
    # Sub Task 4: Jaccard for the _stemmed.txt
    ############################################
    # Create stemmed text
    word_list_edited_stemmed=[]
    for word in word_list_edited:
        word_list_edited_stemmed.append(ps.stem(word))
        
    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        jaccard_similarity=jaccard(word_list_edited_stemmed,word_list_old_edited_stemmed)
        
        output_file.write(";"+str(jaccard_similarity))
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(";")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_edited_stemmed=word_list_edited_stemmed
    
    
    ############################################
    # Sub Task 5: Jaccard for the _stemmed.txt
    # AND REMOVE STOP WORDS - OWN LIST
    ############################################
    # Caution; in general, it is not clear whether you should first stem or
    # first remove stop words.
    # However, in this specific case, you should remove the stop words first
    # and then stem, as your stop word list is based on the inflected text.
    
    # remove stop words using personal stop word list
    word_list_own_filtered=[]
    for word in word_list_edited:
        if word not in own_stop_words:
            word_list_own_filtered.append(word)
    
    # Create stemmed text
    word_list_own_filtered_stemmed=[]
    for word in word_list_own_filtered:
        word_list_own_filtered_stemmed.append(ps.stem(word))
        
    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        jaccard_similarity=jaccard(word_list_own_filtered_stemmed,\
        word_list_old_own_filtered_stemmed)
        
        output_file.write(";"+str(jaccard_similarity))
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(";")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_own_filtered_stemmed=word_list_own_filtered_stemmed
    
    
    ############################################
    # Sub Task 6: Jaccard for the _stemmed.txt
    # AND REMOVE STOP WORDS - NLTK LIST
    ############################################
    # Caution; it is not clear whether you should first stem or first remove
    # stop words. However, the NLTK stop word list seems to be based on inflected
    # text, e.g. the word "having" is included. "Having" would be stemmed to "have".
    # Thus, the stop list seems to be not stemmed.
    # Thus, you should remove the stop words first and then stem.
    
    # remove stop words using NLTK stop word list
    word_list_NLTK_filtered=[]
    for word in word_list_edited:
        if word not in NLTK_stop_words:
            word_list_NLTK_filtered.append(word)
    
    # Create stemmed text
    word_list_NLTK_filtered_stemmed=[]
    for word in word_list_NLTK_filtered:
        word_list_NLTK_filtered_stemmed.append(ps.stem(word))
    
    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        jaccard_similarity=jaccard(word_list_NLTK_filtered_stemmed,\
        word_list_old_NLTK_filtered_stemmed)
        
        output_file.write(";"+str(jaccard_similarity))
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(";")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_NLTK_filtered_stemmed=word_list_NLTK_filtered_stemmed
    
    
    # Write line break to output file
    output_file.write("\n")
    
    # Close 10-K filing
    input_file_10_k.close()
    
input_file.close()
output_file.close()
stop_word_file.close()
print("Task done!")

