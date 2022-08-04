# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""

import re

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the dictionary
file_word_list=open(directory+'Complex_Words.txt','r',encoding="utf-8")
word_list=file_word_list.read()
word_list=word_list.lower()
complex_words=word_list.split()

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_Output_Complex_Tone.csv','w',encoding="utf-8")
output_file.write('CIK;Filename;Number_Words;Number_Complex_Words;Percent_Complex_Words\n')

# Split the input file in separate lines
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
    input_text_10_k=input_file_10_k.read()
    
    # Use lower case letters
    text=input_text_10_k.lower()    
    
    # Split the text in words to determine the total number of words
    list_of_words=re.split('\W{1,}', text)
     # to make sure that empty list elements do not bias the word count, we delete them.
    while list_of_words.count("")>0:
        list_of_words.remove("")
        
    # Determine total number of words
    word_count=len(list_of_words)
    
    # Reset the number of complex words to zero
    complex_count=0
    # For each complex word, count the number of occurrences
    for i in range(len(complex_words)):
        complex_count=complex_count+list_of_words.count(complex_words[i])
    
    # Write cik, file name, total number of words, and number of complex words to output file
    output_file.write(cik+';'+filename+'_clean.txt;'+str(word_count)+';'\
    +str(complex_count)+';'+str(complex_count/word_count)+'\n')
    
    # Close filings
    input_file_10_k.close()    

print("Finished")        
output_file.close()
input_file.close()