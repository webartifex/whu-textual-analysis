# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""

# We split the text into words and sentences using regular expression
import re
# For comparison, we also include the NLTK tokenizer
from nltk.tokenize import sent_tokenize

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_Output_WPS.csv','w',encoding="utf-8")
# Write variable names to the first line of the output file
output_file.write('CIK;Filename;Number_Words;Number_of_Sentences;'\
'Number_of_Sentences_1;Number_of_Sentences_2;Number_of_Sentences_false;'\
'Number_of_Sentences_NLTK;WPS;WPS_1;WPS_2;WPS_false;WPS_NLTK\n')

# Split the Input File in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

# Loop over all lines
for i in range(1,len(input_text_line)):
    print(str(i))
    # split the line into the two variables
    variables=input_text_line[i].split(";")
    # We need the CIK and the filename
    cik=variables[0]
    filename=variables[1]
    filename=filename.replace('.txt','')
    
    # Open the ith 10-K in the list
    input_file_10_k=open(directory+'10-K_Sample/'+cik+"_"+filename+'_clean.txt','r',\
    encoding='ascii',errors='ignore')
    text=input_file_10_k.read()
    
    # Determine number of sentences and number of words    
    # Split the text in words to determine the total number of words
    list_of_words=re.split('\W{1,}', text)
     # to make sure that empty list elements do not bias the word count, we delete them.
    while list_of_words.count("")>0:
        list_of_words.remove("")
    # Determine total number of words
    word_count=len(list_of_words)
    
    
    # Split the text by symbols that indicate the end of a sentence
    # to determine the total number of sentences
    list_of_sentences=re.split('[\.!\?]{1,}', text)
    while list_of_sentences.count("")>0:
        list_of_sentences.remove("")
    # Alternative 1:
    list_of_sentences_1=re.split('(?:\.|!|\?){1,}', text)
    while list_of_sentences_1.count("")>0:
        list_of_sentences_1.remove("")
    # Alternative 2:
    list_of_sentences_2=re.split('\.{1,}|!{1,}|\?{1,}', text)
    while list_of_sentences_2.count("")>0:
        list_of_sentences_2.remove("")
    # Incorrect approach:
    # re.split splits the string by the occurrences of the pattern.
    # If capturing parentheses, i.e. (), are used in pattern, then the text
    # of all groups in the pattern are also returned as part of the resulting list. 
    # See https://docs.python.org/3/library/re.html#re.split for details
    list_of_sentences_false=re.split('(\.|!|\?){1,}', text)
    while list_of_sentences_false.count("")>0:
        list_of_sentences_false.remove("")
    
    # For comparison, we also include the NLTK tokenizer
    list_of_sentences_nltk=sent_tokenize(text)
    
    # Determine total number of sentences
    sentence_count=len(list_of_sentences)
    sentence_count_1=len(list_of_sentences_1)
    sentence_count_2=len(list_of_sentences_2)
    sentence_count_false=len(list_of_sentences_false)
    sentence_count_nltk=len(list_of_sentences_nltk)
    
    # Ratio of # of words over # of sentences
    wps=word_count/sentence_count
    wps_1=word_count/sentence_count_1
    wps_2=word_count/sentence_count_2
    wps_false=word_count/sentence_count_false
    wps_nltk=word_count/sentence_count_nltk
    
    # Write cik, file name, total number of words, total number of sentences,
    # and WPS to the output file
    output_file.write(cik+';'+filename+'_clean.txt;'+str(word_count)+';'+\
    str(sentence_count)+';'+str(sentence_count_1)+';'+str(sentence_count_2)+';'+\
    str(sentence_count_false)+';'+str(sentence_count_nltk)+';'+str(wps)+';'+\
    str(wps_1)+';'+str(wps_2)+';'+str(wps_false)+';'+str(wps_nltk)+'\n')
    
    # Close filing
    input_file_10_k.close()
    

print("Finished") 
output_file.close()
input_file.close()