# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""

import re

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the dictionary
# The dictionary has been obtained from Bill McDonald's webpage
# http://www3.nd.edu/~mcdonald/Word_Lists.html
# --> LoughranMcDonald_MasterDictionary_2014.xlsx
# --> select negative words and copy them to a txt file
file_word_list=open(directory+'LMD_Neg.txt','r',encoding="utf-8")
word_list=file_word_list.read()
# LOOK AT THE FILE. ARE THE WORDS IN UPPER OR IN LOWER CASE?
# MAKE SURE THAT YOU USE A CONSISTENT FORMAT FOR THE TEXT AND THE DICTIONARY.
# THE COMMANDS ARE .lower() AND .upper().

# CREATE A LIST OF NEGATIVE WORDS -> SPLIT THE TEXT
negative_words=word_list.XXXX


# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the input file in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_Output_Negative_Tone.csv','w',encoding="utf-8")
# Write variable names to the first line of the output file
output_file.write('CIK;Filename;Number_Words;Number_Negative_Words;\
Percentage_Negative_Words\n')

# Loop over all lines of the csv file
for i in range(1,len(input_text_line)):
    # If the execution of your scripts takes some time, printing the loop iterator
    # gives you an impression of the overall progress made.
    print(str(i))
    
    # split the line into the two variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (2nd column)
    cik=variables[0]
    filename=variables[1]
    
    # modify file name to open the edited files
    filename=filename.replace('.txt','')
    # Open the ith 10-Ks in the list
    input_file_10_k=open(directory+'10-K_Sample_clean/'+cik+'_'+filename+'_clean.txt','r',\
    encoding='ascii',errors='ignore')
    input_text_10_k=input_file_10_k.read()
    
    # CONVERT THE TEXT TO UPPER OR LOWER CASE (see comment above)
    # It is important that the formatting (lower case vs. upper case) of the word list
    # and the document is identical. Remember that you have typically lower and upper case
    # letters in documents -> modify text
    text=input_text_10_k.XXXXXX
    
    # Split the text in words to determine the total number of words
    # LOOK AT THE REGEX INTRODUCTION FOR A SUITABLE SPLIT VARIABLE. 
    list_of_words=re.split(XXXXX, text)
    
    # ARE THERE EMPTY ELEMENTS IN THE LIST OF WORDS?
    # Make sure that empty list elements do not bias the word count -> delete them!
    # You can use an approach similar to the one in lines 37 and 38.
    COMMANDS TO BE ADDED
        
    # Determine the total number of words
    # COUNT THE NUMBER OF ELEMENTS IN list_of_words
    word_count=XXXX
    
    # Reset the number of negative words to zero
    negative_count=0
    # For each negative word, count the number of occurrences
    for j in range(len(negative_words)):
        
        HERE YOU NEED TO COUNT HOW OFTEN THE jth NEGATIVE WORD IS FOUND IN THE TEXT.
        COMPARE THE TWO CASES BELOW -> EXECUTE THE COMMANDS (see lines below) IN
        THE COMMAND LINE AND COMPARE THE RESULTS.
        WHICH ALTERNATIVE IS THE RIGHT APPROACH?
        
        ALTERNATIVE 1:
        list_of_words=["abandon","abandoned","abandonment"]
        list_of_words.count("abandon")
        ALTERNATIVE 2:
        text_of_words="abandon abandoned abandonment"
        text_of_words.count("abandon")
        
        ADD THE CORRECT COUNT OF NEGATIVE WORD j TO YOUR OVERALL COUNT.
        negative_count=negative_count+XXXXX
    
    # Get the percentage of negative words
    percentage_negative=negative_count/word_count
    
    # Write cik, file name, total number of words, number of negative words,
    # and the percentage of negative words to output file.
    output_file.write(cik+';'+filename+'_clean.txt;'+str(word_count)+';'\
    +str(negative_count)+';'+str(percentage_negative)+'\n')
    
    # Close filings
    input_file_10_k.close()

print("Finished")    
output_file.close()
input_file.close()
