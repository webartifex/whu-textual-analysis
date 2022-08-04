# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe University Frankfurt
"""

# We need regular epressions, tokenize (to identify words), and stemming.
import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 10-Ks from MSFT, KO, and 3M.
input_file=open(directory+'list_10-K_filings_textual_similarity.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the Input File in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

# Loop over all lines
#for i in range(1,len(input_text_line)):
# for illustration filings 1 to 3 only
for i in range(1,4):
    print(str(i))
    # split the line into the eight variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (8th column)
    cik=variables[0]
    filename_parts=re.split('/',variables[7])
    filename=filename_parts[3].replace('.txt','')
    
    # Open the ith 10-K in the list; remember to specify the encoding
    input_file_10_k=open(directory+'10-K_Textual_Similarity/'+cik+'_'+filename\
    +'_edited.txt', 'r', encoding='ascii', errors='ignore')
    # Get the text of the 10-K
    input_text_10_k=input_file_10_k.read()
    
    # We need to tokenize the text because stem only works on a word by word basis.
    # Stemming an entire document without splitting into words does not work!
    # The problem is that \n gets lost in this process --> we cannot easily 
    # recreate the document.
    # idea: replace \n by \n and some indicator that there was a line break.
    # Here, I choose "LINEBREAKMARK"
    input_text_10_k=input_text_10_k.replace("\n","\nLINEBREAKMARK ")
    
    # Split text into words
    # There are two alternatives.
    # Alternative 1 (our standard approach):
    #word_list=re.split("\W{1,}",input_text_10_k.lower())
    # Alternative 2 (keeps symbols like ,;.):
    word_list=word_tokenize(input_text_10_k.lower())


    # Stem the text
    text_stemmed=''
    for word in word_list:
        # The following two cases are designed to improve the formatting of the
        # output file. It is not needed for the subsequent analyses.
        
        # Case 1: 'word' is not an actual word but a symbol. -> there should
        # be no whitespace between the previous words and this symbol.
        # \A and \Z indicate the beginning and end of string -> the 'word' is just
        # the symbol but not a combination of letters and symbols.
        
        if re.search("\A[\.\?!,:;']{1,}\Z",word):
            text_stemmed=text_stemmed+word
        # Case 2: the word is an actual word -> have a whitespace included.
        else:
            text_stemmed=text_stemmed+" "+PorterStemmer().stem(word)
        
        # The simple solution (without restoring the formatting of the text) is:
        #text_stemmed=text_stemmed+" "+PorterStemmer().stem(word)
        
        
    # To recreate the text, we need to replace the line break indicators by \n
    # Because of the stemming "LINEBREAKMARK" becomes "linebreakmark".
    text_stemmed=text_stemmed.replace("linebreakmark","\n")
    
    
    # Open the output file for the stemmed text
    output_file_10_k=open(directory+'10-K_Textual_Similarity/'+cik+'_'+filename\
    +'_stemmed.txt', 'w', encoding='ascii', errors='ignore')
    output_file_10_k.write(text_stemmed)
    output_file_10_k.close()
    input_file_10_k.close()

input_file.close()
print("Task done!")