# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:43:32 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""

import re

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the dictionary
# The dictionary has been obtained from Bill McDonald's webpage
# http://www3.nd.edu/~mcdonald/Word_Lists.html
# --> LoughranMcDonald_MasterDictionary_2014.xlsx
# --> select negative words and copy them to a txt file
file_word_list=open(directory+'LMD_Neg.txt','r',encoding="utf-8")
word_list=file_word_list.read()
# The LMD words are all in upper case
word_list=word_list.lower()
negative_words=word_list.split('\n')

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
#for i in range(1,10):
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
    input_file_10_k=open(directory+'10-K_Sample/'+cik+'_'+filename+'_clean.txt','r',\
    encoding='ascii',errors='ignore')
    # if the command above does not work (error like "file not found" or "directory not found")
    # please use the following command:
    #input_file_10_k=open(directory+'10-K_Sample_clean/'+cik+'_'+filename+'_clean.txt','r',encoding='ascii',errors='ignore')
    input_text_10_k=input_file_10_k.read()
    
    # Use lower case letters, too
    # It is important that the formatting (lower case vs. upper case) of the word list
    # and the document is identical. Remember that you have typically lower and upper case
    # letters in documents -> modify text.
    text=input_text_10_k.lower()   
    
    # Split the text in single words to determine the total number of words
    # \W is a non-word character: "Matches any character which is not a Unicode
    # word character." (Python documentation)
    # this is equivalent to [^a-zA-Z0-9_], i.e. no lower case letters, no upper
    # case letters, no numbers, and no underscore.
    list_of_words=re.split('\W{1,}', text)
    # to make sure that empty list elements do not bias the word count, we delete them.
    while list_of_words.count("")>0:
        list_of_words.remove("")
    # It is important that you treat multiple "\W" as one. Otherwise you are left
    # with elements in the list that are not acutal words.
    
    # Determine the total number of words
    word_count=len(list_of_words)
    
    # Reset the number of negative words to zero
    negative_count=0
    # For each negative word, count the number of occurrences
    for j in range(len(negative_words)):
        # the command "list_of_words.count(negative_words[i])" only matches if there
        # is exact overlap between the ith negative word and the words in the list.
        # For example the following two commands:
        # list_of_words=["abandon","abandoned","abandonment"]
        # list_of_words.count("abandon")
        # yields 1 match
        # In contrast,
        # text_of_words="abandon abandoned abandonment"
        # text_of_words.count("abandon")
        # yields 3. Thus, you have to split the text to individual words!!!
        negative_count=negative_count+list_of_words.count(negative_words[j])
    
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
