# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:37:49 2022

@author: Alexander Hillert, Goethe University
"""

# import packages
import re
import nltk
import collections

# define working directory
# adjust it to your computer
directory = "YOUR DIRECTORY"

# =============================================================================
# Part A: Identifying the answers to market-related sentences
# =============================================================================

# Create output file
output_csv_file_3a = open(directory+'Problem_3a_Market-related_Questions.csv', 'w', encoding="utf-8")
# Write variable names to the first line of the output file
# 1) Call-ID
# 2) Number of questions in the call
# 3) The number of market-related questions
# 4) The percentage of market-related questions
output_csv_file_3a.write('Call_ID;Number_Questions;Number_Market_Questions;Percetage_Market_Questions\n')

# create a text variable to store managers answers to market-related questions
answers_market_questions=""

# Iterate over the 60 questions and answer files respectively
for i in range(1, 61):

    # If the execution of your scripts takes some time, printing the iterator
    # gives you an impression of the overall progress
    print(str(i))
        
    # reset variables
    market_question_count=0

    
    # Open the ith question file
    # IF YOU HAVE PROBLEMS OPENING THE FILES DOUBLE-CHECK THE DIRECTORY AND FOLDER NAME
    input_file_question = open(directory+'/Problem_2_3_Sample_QandA/'+str(i)+'_questions.txt', 'r',
                               encoding='utf-8', errors='ignore')
    # read the text from the question file
    input_text_question=input_file_question.read()
    
    # To identify managements' answer to a market-related question, also open the
    # answer files and create a list of the individual answers.
    # the jth list element in the answer list will correspond to the jth list 
    # element in the question list.
    # Open the ith answer file
    input_file_answer = open(directory+'/Problem_2_3_Sample_QandA/'+str(i)+'_answers.txt', 'r',
                             encoding='utf-8', errors='ignore')
    input_text_answer=input_file_answer.read()
    
    
    # Split the text into individual questions
    question_list = re.split(TO BE COMPLETED, text_questions)
    # Check whether there are empty questions, if so remove them
    while TO BE COMPLETED > 0:
        TO BE COMPLETED
        
    # get the total number of questions    
    number_questions=TO BE COMPLETED
    
    
    # Split the text into individual answers
    answer_list = re.split(TO BE COMPLETED, input_text_answer)
    # Check whether there are empty questions, if so remove them
    while TO BE COMPLETED > 0:
        TO BE COMPLETED

    # search for the term market/markets in each analyst question
    # iterate over the list of questions
    for j in range(TO BE COMPLETED):
        question_id=j+1
        
        # it might be helpful to get the text of a question to a new variable
        # of course, you can also work with the jth element of the question list.
        question_text=TO BE COMPLETED
        
            
        # search for market/markets in the list of words
        
        # remember that searching for a word in a text is NOT the same as searching
        # for a word in a list. Make sure that you only count actual matches!!!
        # ADD necessary commands here
        YOU MAY NEED TO ADD A COMMAND HERE.
        
        # Are there upper case letters? Are there lower case letters?
        # Remember to use a consistent format of the text and the search term.
        
        if TO BE COMPLETED.count("market")>0 or TO BE COMPLETED:
            # it is a market-related question
            market_question_count=TO BE COMPLETED
            
            
            # For Part b) you need the text of the answers to market-related
            # questions. So, we identify the corresponding answer.
            # question j relates to answer j.
            # --> pick the right element from the answer list
            market_answer=TO BE COMPLETED
            
            # add the text of answer j to the total text of all answers
            answers_market_questions=answers_market_questions+"\n"+market_answer
    
    
    # compute the percentage of market-related questions
    pct_mkt_questions=TO BE COMPLETED
    
    
    # Write the call-ID, the total number of questions, the number of market questions,
    # and the percentage of market questions to the output file
    output_csv_file_3a.write(str(i)+';'+str(number_questions)+';'+str(market_question_count)+';' +
                          str(pct_mkt_questions)+'\n')
    
# close files
output_csv_file_3a.close() 

print("Part a) of Problem 3 completed.")

# =============================================================================
# Part B: Most frequent trigrams in the answers to market-related questions
# =============================================================================    

# import english stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
NLTK_stop_words=set(stopwords.words('english'))

# import sentence tokenizer
# even though we discussed the weaknesses of the tokenizer in class, for this 
# text corpus it is fine to use the tokenizer.
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# list and counter for building trigrams
trigram_list=[]
trigram_counter=collections.Counter()


# Create output file
output_csv_file_3b = open(directory+'Problem_3b_Most_Frequent_Trigrams.csv', 'w', encoding="utf-8")
# Write variable names to the first line of the output file
# 1) rank of the trigram ranging from 1 to 30
# 2) trigram
# 3) frequency of the trigram
output_csv_file_3b.write('Rank;Trigram;Frequency\n')

# the managers' answers to market related sentences are stored in the text variable
# "answers_market_questions"

  
# split the entire answer text into single sentences
list_sentences=TO BE COMPLETED

# iterate all sentences
for i in range(TO BE COMPLETED):
    # transform the ith sentence to lower or to upper case.
    # make sure that the upper/lower case spelling is consistent with the
    # stop word list!
    sentence=TO BE COMPLETED
    
    # remove numbers
    sentence=TO BE COMPLETED
    # delete single letter words
    sentence=TO BE COMPLETED
    
    # split the sentence into words
    list_of_words=TO BE COMPLETED
    # remove empty elements from the list of words
    while TO BE COMPLETED>0:
        TO BE COMPLETED
    
    # remove stopwords
    list_of_nonstop_words=[]
    for TO BE COMPLETED:
        if TO BE COMPLETED:
            list_of_nonstop_words.append(TO BE COMPLETED)
            
    # go over all potential three word combinations in the sentence.
    # check whether you have at least three words remaining in the sentence.
    if len(TO BE COMPLETED)>=3:
        # go over all words in the sentence.
        # remember to pay attention to the upper bound. For example, if there
        # are 5 words in a sentence, you can only form 3 trigrams
        for TO BE COMPLETED:
            # append the three words of the trigram to the list of trigrams
            # put a single whitespace between the three single words.
            trigram_list.append(TO BE COMPLETED+' '+TO BE COMPLETED+' '+TO BE COMPLETED)  


# add the list of trigrams to the counter of trigrams
trigram_counter=collections.Counter(TO BE COMPLETED)

# Get the 30 most frequent trigrams
top_30_trigrams=TO BE COMPLETED

# Write the 30 most frequent trigrams to the csv file.
# Remember Python starts counting at 0, while humans start at 1.
# So, the most frequent word (rank 1 in human counting) is element 0 for Python.
# Consequently, to get a consistent table, we must use the value i for the rank
# but call the element i-1.
for i in range(TO BE COMPLETED):
    output_csv_file_3b.write(str(i)+";"+str(TO BE COMPLETED)+";"+\
    str(TO BE COMPLETED)+"\n")


# close files
output_csv_file_3b.close()

print("Part b) of the Problem has also been completed.")
