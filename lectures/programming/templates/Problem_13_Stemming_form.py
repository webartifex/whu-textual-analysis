# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe University Frankfurt
"""

# We need regular epressions and stemming.
import re
from nltk.stem import PorterStemmer
# Depending on how you would like to split the text in words, you may need tokenize.
from nltk.tokenize import word_tokenize

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 10-Ks from MSFT, KO, and 3M
input_file=open(directory+'list_10-K_filings_textual_similarity.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the Input File in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

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
    input_file_10_k=open(directory+'10-K_Textual_Similarity_edited/'+cik+'_'+filename\
    +'_edited.txt', 'r', encoding='ascii', errors='ignore')
    # if the command above does not work (error like "file not found" or "directory not found")
    # please use the following command:
    #input_file_10_k=open(directory+'10-K_Textual_Similarity/'+cik+'_'+filename+'_edited.txt','r',encoding='ascii',errors='ignore')
    
    
    # Get the text of the 10-K
    input_text_10_k=input_file_10_k.read()
    
    # We need to tokenize the text because stem only works on a word by word basis.
    # Stemming an entire document without splitting into words does not work!
    # The problem is that \n gets lost in this process --> we cannot easily 
    # recreate the document.
    # Solution: replace \n by \n and some indicator that there was a line break.
    # For example replace("\n","\nHereWasALinebreak")
    input_text_10_k=input_text_10_k.replace("\n",XXXX)
    
    # Split text into words
    word_list=XXXX

    # Stem the text from above
    text_stemmed=''
    # LOOP ALL WORDS, STEM THEM AND RECONNECT THEM.
    # WARNING: WHEN RECONNECTING WORDS YOU NEED TO INCLUDE A WHITESPACE BETWEEN
    # THE WORDS. OTHERWISE, THE TEXT GETS MESSED UP.
    for word in word_list:
        
        text_stemmed=text_stemmed+XXX # TO BE COMPLETED
        
    # To recreate the text, we need to replace the line break indicators by \n.
    # WARNING: PAY ATTENTION TO UPPER/LOWER CASE, IT CAN CHANGE.
    text_stemmed=text_stemmed.replace(XXXX,XXXX) # UNDO THE TRANSFORMATION FROM LINE 56.
    
    
    # Open the output file for the stemmed text
    output_file_10_k=open(directory+'10-K_Textual_Similarity_edited/'+cik+'_'+filename\
    +'_stemmed.txt', 'w', encoding='ascii', errors='ignore')
    output_file_10_k.write(text_stemmed)
    output_file_10_k.close()
    input_file_10_k.close()

input_file.close()
print("Task done!")