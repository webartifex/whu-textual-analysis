# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe University Frankfurt
"""

# For the full task, we need a large set of packages:
# regular expression, stemming, stop words, tokenization, and counters.
import re
#from nltk.tokenize import word_tokenize # NOT needed for the base comparison
#from nltk.corpus import stopwords # NOT needed for the base comparison
#from nltk.stem import PorterStemmer # NOT needed for the base comparison
from collections import Counter


#ps=PorterStemmer() # NOT needed for the base comparison

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 10-Ks from MSFT, KO, and 3M
input_file=open(directory+'list_10-K_filings_textual_similarity.csv','r',encoding="utf-8")
input_text=input_file.read()

# Split the input file in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")

# Open the output csv file in which we write the similarities
output_file=open(directory+'list_10-K_filings_textual_similarity_jaccard.csv','w',encoding="utf-8")
# Write variable names to first line
output_file.write(input_text_line[0]+';Jaccard\n')


# set default values for variables
word_list_old_edited=""
word_list_edited=""

# Loop over all lines
for i in range(1,len(input_text_line)):
    print(str(i))
    # split the line into the eight variables
    variables=input_text_line[i].split(";")
    # We need the CIK (1st column) and the filename (8th column)
    cik=variables[0]
    filename_parts=re.split('/',variables[7])
    filename=filename_parts[3].replace('.txt','')
    
    # Open the ith 10-K; remember to specify the encoding
    input_file_10_k=open(directory+'10-K_Textual_Similarity_edited/'+cik+'_'+filename+\
    '_edited.txt', 'r', encoding='ascii', errors='ignore')
    # if the command above does not work (error like "file not found" or "directory not found")
    # please use the following command:
    #input_file_10_k=open(directory+'10-K_Textual_Similarity/'+cik+'_'+filename+'_edited.txt','r',encoding='ascii',errors='ignore')
    
    
    input_text_10_k=input_file_10_k.read()
    
    # Split text into words
    word_list_edited=re.split("\W{1,}",input_text_10_k.lower())
    # Alternative using tokenize
    #word_list_edited=word_tokenize(input_text_10_k.lower())
    
    # check whether the previous entry of the list is from the same firm
    permco=input_text_line[i].split(";")[1]
    permco_old=input_text_line[i-1].split(";")[1]
    
    
    ############################################
    # Sub Task 1: Jaccard for the _edited.txt
    ############################################
    # compute Jaccard similarity if the previous filing is from the same firm
    if permco==permco_old:
        
        counter_current_10k=Counter(XXX)
        counter_previous_10k=Counter(XXX)

        intersection=XXX see "Introduction_Container_Datatypes.py" (at the end of the file)
        union=XXXX see "Introduction_Container_Datatypes.py" (at the end of the file)

        jaccard_similarity=XXXx # ELEMENTS IN INTERSECTION / # ELEMENTS IN UNION 
        output_file.write(input_text_line[i]+";"+str(jaccard_similarity)+"\n")
    else:
        # The previous filing is not from the same firm -> cannot compute Jaccard similarity
        output_file.write(input_text_line[i]+";"+"\n")
    
    # Save the current word vector to a separate variable for the comparison of the next report.
    word_list_old_edited=word_list_edited
    
    # Close 10-K filing
    input_file_10_k.close()
    
input_file.close()
output_file.close()
print("Task done!")

