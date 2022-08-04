# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert
"""

import re

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the dictionary
# The dictionary is obtained from Bill McDonald's webpage
# http://www3.nd.edu/~mcdonald/Word_Lists.html
# --> LoughranMcDonald_MasterDictionary_2014.xlsx
# --> select positive words and copy them to a txt file
file_word_list=open(directory+'LMD_Pos.txt','r',encoding="utf-8")
word_list=file_word_list.read()
word_list=word_list.lower()
positive_words=word_list.split()

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the Input File in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")
    
# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_Output_Positive_Tone.csv','w',encoding="utf-8")
# Write variable names to the first line of the output file
output_file.write('CIK;Filename;Number_Words;Number_Pos_Words;Number_Pos_Words_adj;'\
+'Percent_Pos_Words;Percent_Pos_Words_adj\n')

# Iterate the list of the 200 10-K filings
# the last line is empty --> loop only up to len()-1
#for i in range(1,len(input_text_line)):
for i in range(1,20): # For illustration only
    # If the execution of your scripts takes some time, printing the iterator
    # gives you an impression of the overall progress
    print(str(i))
    
    # split the line into the two variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (2nd column)
    cik=variables[0]
    filename=variables[1]
    
    # modify file name to open the edited files
    filename=filename.replace('.txt','')
    
    # Open the ith 10-K in the list
    input_file_10_k=open(directory+'/10-K_Sample/'+cik+"_"+filename+'_clean.txt','r',\
    encoding='ascii',errors='ignore')
    # if the command above does not work (error like "file not found" or "directory not found")
    # please use the following command:
    #input_file_10_k=open(directory+'10-K_Sample_clean/'+cik+'_'+filename+'_clean.txt','r',encoding='ascii',errors='ignore')
    input_text_10_k=input_file_10_k.read()
    
    # Use lower case letters, too
    # It is important that the formatting (lower case vs. upper case) of the word list
    # and the document are identical. Remember that you have typically lower and upper case
    # letters in documents -> modify text
    text=input_text_10_k.lower()
    
    # Split the text in single words to determine the total number of words
    list_of_words=re.split('\W{1,}', text)
    # to make sure that empty list elements do not bias the word count, we delete them.
    while list_of_words.count("")>0:
        list_of_words.remove("")
        
    # Determine total number of words
    word_count=len(list_of_words)
    
    # Reset the number of positive words and positive words adj. for negations to zero
    positive_count=0
    positive_count_adj=0
    # For each positive word, count the number of occurrences
    for j in range(len(positive_words)):
        # standard count operation without controlling for negations
        positive_words_found=list_of_words.count(positive_words[j])
        
        # Loughran and McDonald (2011, JF, p.44): "We account for simple negation
        # only for Fin-Pos words. Simple negation is taken to be observations
        # of one of six words (no, not, none, neither, never, nobody) occurring
        # within three words preceding a positive word.
        
        # When we have identified positive words we need to search for negations
        while positive_words_found>0:
            # identify the position of the matched positive word in the list of all words
            position_of_word=list_of_words.index(positive_words[j])
            # identify the three words before the positive word and add them to a list
            # the \ is a line break
            list_negation=[list_of_words[max(0,position_of_word-3)],\
            list_of_words[max(0,position_of_word-2)],list_of_words[max(0,position_of_word-1)]]
            # check whether one of the three words in list_negation is a negation
            negation_found=list_negation.count('no')+list_negation.count('not')+\
            list_negation.count('none')+list_negation.count('neither')+\
            list_negation.count('never')+list_negation.count('nobody')
            
            if negation_found==0:
                # no negation
                positive_count_adj=positive_count_adj+1
                positive_count=positive_count+1
            else:
                # negation
                positive_count=positive_count+1
    
             # delete the matched positive words in the original document 
            list_of_words[position_of_word]=''
            # check whether there are further matches of the jth positive word
            positive_words_found=list_of_words.count(positive_words[j])
            
    # Write cik, file name, total number of words, and number of positive
    # and adjusted positive words to the output file
    output_file.write(cik+';'+filename+'_clean.txt;'+str(word_count)+';'+\
    str(positive_count)+';'+str(positive_count_adj)+';'+str(positive_count/word_count)+\
    ';'+str(positive_count_adj/word_count)+'\n')
    
    # Close filings
    input_file_10_k.close()
    
print("Finished")
output_file.close()
input_file.close()