# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert
"""

import re

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the dictionary
# The dictionary is obtained from Bill McDonald's webpage
# http://www3.nd.edu/~mcdonald/Word_Lists.html
# --> LoughranMcDonald_MasterDictionary_2014.xlsx
# --> select positive words and copy them to a txt file
file_word_list=open(directory+'LMD_Pos.txt','r',encoding="utf-8")
word_list=file_word_list.read()

# LIKE IN PROBLEM 7, YOU HAVE TO APPLY A CONSISTENT FORMAT TO BOTH THE LMD-WORDS
# AND THE TEXT OF THE 10-Ks.
positive_words=word_list.split()

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the Input File in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the iput file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_Output_Positive_Tone.csv','w',encoding="utf-8")
# Write variable names to the first line of the output file
output_file.write('CIK;Filename;Number_Words;Number_Pos_Words;Number_Pos_Words_adj;'\
+'Percent_Pos_Words;Percent_Pos_Words_adj\n')


# Iterate the list of the 200 10-K filings
for i in range(1,len(input_text_line)):
    # If the execution of your scripts takes some time, printing the iterator
    # gives you an impression of the overall progress made.
    print(str(i))
    
    # split the line into the two variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (2nd column)
    cik=variables[0]
    filename=variables[1]
    
    # modify file name to open the edited files
    filename=filename.replace('.txt','')
    
    # Open the ith 10-K in the list
    input_file_10_k=open(directory+'/10-K_Sample_clean/'+cik+"_"+filename+'_clean.txt','r',\
    encoding='ascii',errors='ignore')
    input_text_10_k=input_file_10_k.read()
    
    # It is important that the formatting (lower case vs. upper case) of the word list
    # and the document are identical. Remember that you have typically lower and upper case
    # letters in documents -> modify text
    text=XXXX # CONSISTENT FORMAT
    
    # Split the text in single words to determine the total number of words
    list_of_words=re.split(XXXX, text) # USE THE SAME COMMAND AS IN PROBLEM 7
    
    # ARE THERE EMPTY ELEMENTS IN THE LIST OF WORDS?
    # Make sure that empty list elements do not bias the word count -> delete them!
    # You can use an approach similar to the one in lines 34 and 35.
    COMMANDS TO BE ADDED   
    
    # Determine total number of words
    word_count=XXXX # SAME COMMAND AS IN PROBLEM 7
    
    # Reset the number of positive words and positive words adj. for negations to zero.
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
            position_of_word=list_of_words.XXXXX # THE COMMAND .index() IS HELPFUL HERE
            
            # identify the three words before the positive word and add them to a list
            list_negation=[3_WORDS_BEFORE_MATCH,2_WORDS_BEFORE_MATCH,1_WORD_BEFORE_MATCH]
            # REPLACE THE THREE PLACEHOLDERS BY THE CORRESPONDING ELEMENTS OF list_of_words
            
            # check whether one of the three words in list_negation is a negation
            negation_found=list_negation.count('no')+list_negation.count('not')+XXXX TO BE COMPLETED
            
            if negation_found==0:
                # no negation
                positive_count_adj=positive_count_adj+1
                positive_count=positive_count+1
            else:
                # negation
                positive_count=positive_count+1
    
             # delete the matched positive words in the original document
            list_of_words[position_of_word]=XXX
            # THIS OPERATION IS IMPORTANT BECAUSE OTHERWISE WE WILL GET AN ENDLESS LOOP
            
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