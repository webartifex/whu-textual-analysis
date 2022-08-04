# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:42:03 2022

@author: Alexander Hillert, Goethe University
"""

# import packages
import re

# define working directory
# adjust it to your computer
directory = "YOUR DIRECTORY"


# Open the dictionary
# It is the 2018 version of the LM (2011) dictionary.
file_word_list = open(directory+'LMD_pos_master_dictionary_2018.txt', 'r', encoding="utf-8")
word_list = file_word_list.read()
# use a consistent case format
word_list = TO BE COMPLETED
# create the list of positive words
positive_words = TO BE COMPLETED


# Create output file according to the exam instructions
output_csv_file = open(directory+'Problem_2a_Percentage_Positive_Words.csv', 'w', encoding="utf-8")
# Write variable names to the first line of the output file
# 1) Call-ID
# 2) Answer-ID
# 3) Total number of words in the answer
# 4) The number of positive words in the answer
# 5) The percentage of positive words in the answer
# 6) the text of the answer
output_csv_file.write('TO BE COMPLETED')


# Iterate over the 60 answer files
for i in range(TO BE COMPLETED):
    # If you want you can print the progress of your script
    print(str(i))
    

    # Open the ith answer file
    input_file_answer = open(directory+'/Problem_2_3_Sample_QandA/'+TO BE COMPLETED, 'r',
    encoding='utf-8', errors='ignore')

    # read the text from the answer file
    input_text_answer = input_file_answer.read()
    
    # use a consistent case format
    input_text_answer = 

    # Split the text into individual answers
    answer_list = re.split(TO BE COMPLETED, input_text_answer)

    # Check whether there are empty elements in the answer list
    # If so, remove them
    while answer_list.TO BE COMPLETED:
        TO BE COMPLETED
    
    # iterate all answers of the ith call
    for TO BE COMPLETED:

        # Preprocessing steps according to the exam instructions and hints
        TO BE COMPLETED
        # re.sub() commands are useful here.

        
        ######### Begin of the placeholder #########
        # Here is the placeholder for the further editing steps that you
        # should identify by looking at the file from Part b) of this problem.
        # Having created a first file in Part b), you will see that the measurement
        # of positive tone can be improved.
        # Please add these commands here and then return to part 2b)
        # See also the exam instructions.
        
        
        
        
        ######### End of the placeholder ########
        
        
        # Split the text in words
        list_of_words = TO BE COMPLETED
        # Check for empty elemments
        TO BE COMPLETED
        
        
        # Determine total number of words
        word_count = TO BE COMPLETED

        # Reset the number of positive words to zero
        positive_count = 0
        
        # For each positive word, count the number of occurrences
        for TO BE COMPLETED
            # Check whether the positive word of interest shows up
            positive_words_found = TO BE COMPLETED

            # Loughran and McDonald (2011, JF, p.44): "We account for simple negation
            # only for Fin-Pos words. Simple negation is taken to be observations
            # of one of six words (no, not, none, neither, never, nobody) occurring
            # within three words preceding a positive word.

            # While the positive word is found, implement the LM (2011) negation check.
            while TO BE COMPLETED:
                # identify the position of the matched positive word in the list of all words
                position_of_word = TO BE COMPLETED
                # identify the three words before the positive word 
                list_negation = TO BE COMPLETED
                
                # check whether one of the three words in list_negation is a negation
                negation_found = TO BE COMPLETED

                if negation_found TO BE COMPLETED:
                    positive_count = TO BE COMPLETED

                # delete the matched positive word in the original document
                list_of_words[position_of_word] = TO BE COMPLETED
                # check whether there are further matches of the positive word of interest
                positive_words_found = TO BE COMPLETED

        # compute the percentage of positive words adjusted for negations
        # it could be that the total number of words of an answer is zero.
        if word_count > 0:
            percentage_positive = TO BE COMPLETED
        else:
            percentage_positive = "NA"


        # Remove line breaks of the text that you write to the csv.
        # Line breaks would mess up your output file.
        # In addition to line breaks, you may also want to remove extra
        # whitespaces and tabs at the beginning and end.
        answer_text_print = re.sub(TO BE COMPLETED)
        # replace the symbol that you use as delimiter, e.g., semicolon
        answer_text_print = re.sub(TO BE COMPLETED, answer_text_print)

        # Write the call-ID, answer-ID, total number of words, number of positive words
        # adjusted for negations, percentage of positive words adjusted for negations,
        # and the edited answer text to the output file
        output_csv_file.write(TO BE COMPLETED+'\n')

    # Close files
    input_file_answer.close()

print("Finished")
output_csv_file.close()
