# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:19:54 2017

@author: Alexander Hillert, Goethe University Frankfurt
"""

# We need regular expressions and counters (->collections)
import re
import collections
# for the bigram part, the sentence tokenizer is helpful
from nltk.tokenize import sent_tokenize

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 10-Ks from MSFT, KO, and 3M.
input_file=open(directory+'list_10-K_filings_textual_similarity.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the input file in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

# Create an empty counter variable
words_counter=collections.Counter()
# variable is needed only for an alternative solution
words_counter1=collections.Counter()

# counter for the extra task
bigram_counter=collections.Counter()


# Loop over all lines
for i in range(1,len(input_text_line)):
    print(str(i))
    # split the line into the eight variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (8th column)
    cik=variables[0]
    filename_parts=re.split('/',variables[7])
    filename=filename_parts[3].replace('.txt','')
    
    # Open the ith 10-K in the list; remember to specify the encoding
    # The files are available in the zip file "10-K_Textual_Similarity_edited.zip".
    input_file_10_k=open(directory+'10-K_Textual_Similarity/'+cik+'_'+\
    filename+'_edited.txt', 'r', encoding='ascii', errors='ignore')
    # if the command above does not work (error like "file not found" or "directory not found")
    # please use the following command:
    #input_file_10_k=open(directory+'10-K_Textual_Similarity_edited/'+cik+'_'+filename+'_edited.txt','r',encoding='ascii',errors='ignore')
    
    # read the content from the file
    input_text_10_k=input_file_10_k.read()
    
    # use lower case only so that it does not matter whether a word is at
    # the beginning of a sentence ("The") or within a sentence ("the").
    # Please note that this can be problematic, e.g. "US" -> United States vs.
    # us (personal pronoun)
    input_text_10_k_lower=input_text_10_k.lower()
    
    # Split text into words
    list_of_words=re.split('\W{1,}',input_text_10_k_lower)
    # There can be empty ("") list elements -> remove them
    while list_of_words.count("")>0:
        list_of_words.remove("")
    
    # optional commands to remove words that only contain "_"
    '''
    for word in list_of_words:
        if re.sub("[a-zA-Z]","",word)!="":
        #if word.count("_")>0:
            list_of_words.remove(word)
    '''
    
    # Add the words to our counter
    words_counter=words_counter+collections.Counter(list_of_words)
    # alternative solution
    words_counter1.update(list_of_words)
    
    
    #############################################
    # optional part for the extra task on bigrams
    #############################################
    
    # create an empty list for the bigrams
    bigram_list=[]
    
    # split the text into sentences
    list_of_sentences=sent_tokenize(input_text_10_k)
    
    # create the BIGRAM IN EACH SENTENCE
    for sentence in list_of_sentences:
        
        # make the sentence lower case
        sentence_lower=sentence.lower()
        
        # split the sentence into words
        list_of_words=re.split("\W{1,}",sentence_lower)
        
        # remove empty elements
        while list_of_words.count("")>0:
            list_of_words.remove("")
        
        #print("these are the words of the sentence:\n"+str(list_of_words))
        
        # go over all potential two word combinations in the sentence.
        for word_number in range(0,len(list_of_words)-1):
            bigram_list.append(list_of_words[word_number]+' '+list_of_words[word_number+1])
                
    bigram_counter=bigram_counter+collections.Counter(bigram_list)
    # end of extra task
    
    
    # Close the 10-K filing
    input_file_10_k.close()

input_file.close()

######################
# Top 100 single words
######################
# Open the csv file containing the 100 most frequently used words
output_file=open(directory+'Problem_12_100_most_frequent_words.csv','w',encoding="utf-8")
output_file.write("rank;word;count\n")

# Get the 100 most frequent words
top_100_words=words_counter.most_common(100)
# for the alternative solution
#top_100_words=words_counter1.most_common(100)

# Write the 100 most frequent words to the csv file.
# Remember Python starts counting at 0, while humans start at 1.
# So, the most frequent words (rank 1 in human counting) is element 0 for Python.
# Consequently, to get a consistent table, we must use the value i for the rank
# but call the element i-1.
for i in range(1,101):
    output_file.write(str(i)+";"+str(top_100_words[i-1][0])+";"+\
    str(top_100_words[i-1][1])+"\n")

# Close the csv file
output_file.close()


######################
# Extra task
# Top 100 bigrams
######################
# Open the csv file containing the 100 most frequently used BIGRAMS
output_file_bigram=open(directory+'Problem_12_100_most_frequent_bigrams.csv','w',encoding="utf-8")
output_file_bigram.write("rank;word;count\n")

# Get the 100 most frequent words
top_100_bigrams=bigram_counter.most_common(100)

# Write the 100 most frequent bigrams to the csv file -> same approach as for the single words.
for i in range(1,101):
    output_file_bigram.write(str(i)+";"+str(top_100_bigrams[i-1][0])+";"+\
    str(top_100_bigrams[i-1][1])+"\n")

# Close the csv file
output_file_bigram.close()


print("Task done!")
