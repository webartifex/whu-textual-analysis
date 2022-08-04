# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""

# We split the text into words and sentences using regular expression
import re

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_Output_WPS.csv','w',encoding="utf-8")
# Write variable names to the first line of the output file
output_file.write('CIK;Filename;Number_Words;Number_of_Sentences;WPS\n')

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
    input_file_10_k=open(directory+'10-K_Sample_clean/'+cik+"_"+filename+'_clean.txt','r',\
    encoding='ascii',errors='ignore')
    text=input_file_10_k.read()
    
    # Determine number of sentences and number of words    
    # DETERMINE THE NUMBER OF WORDS; YOU KNOW THE COMMAND FROM PROBLEMS 7 AND 8.
    list_of_words=re.split(XXX, text)
    # Determine total number of words
    word_count=XXX
    # Split the text by symbols that indicate the end of a sentence
    # to determine the total number of sentences
    list_of_sentences=re.split(XXX, text)
    # Determine total number of sentences
    sentence_count=XXX
    
    # Ratio of # of words over # of sentences
    wps=word_count/sentence_count
    
    # Write cik, file name, total number of words, total number of sentences,
    # and WPS to the output file
    output_file.write(cik+';'+filename+'_clean.txt;'+str(word_count)+';'+\
    str(sentence_count)+';'+str(wps)+'\n')
    
    # Close filing
    input_file_10_k.close()
    

print("Finished") 
output_file.close()
input_file.close()