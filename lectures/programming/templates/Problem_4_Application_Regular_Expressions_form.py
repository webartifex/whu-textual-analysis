# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:50:22 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""

# Import regular expressions and BeautifulSoup
import re
from bs4 import BeautifulSoup

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"
# It is important to use a single forward slash / but not a single backslash \.
# For MAC users: your directory will usually start with "/Users/". For example:
#directory="/Users/FirstnameLastname/Textual Analysis/Programming/Files/"

# Open the document
input_file=open(directory+'Exercise_4_Application_Regular_Expressions.txt','r',encoding="utf-8")
input_text=input_file.read()

#######################
# Task 1: remove tables
#######################
# Approach
# We search for tables until we find no more html tags that indicate the
# beginning of a table.
# Search for the start html-tag <TABLE>
table_match=re.search(TO BE COMPLETED, input_text)
while : # YOU NEED A LOOP THAT SEARCHES FOR TABLES
    # When we have identified a match, i.e. the start of a table, we save
    # the position of the beginning of the table in the variable "start_table"
    table_start_match=re.search(XXX, input_text)
    start_table=table_start_match.start()
    # Next, we search for the corresponding html tag that indicates the end of
    # the table and save the end position to the variable "end_table"
    
    # REPEAT THE COMMANDS ABOVE FOR THE END OF TABLE
    table_end_match=
    end_table=
    
    # We can print the text between the start and end html tag to check whether
    # the table has been identified correctly.
    print("The text below is a table!\n"+input_text[start_table:end_table])

    # the text between the beginning and end of the html tags is the part which
    # we would like to delete.
    # Consequently, we keep the text before the beginning of the table as well
    # as the text after the ending of the table.
    input_text=TO BE COMPLETED
    # Next, we need to check whether there is another table in the rest of the
    # text.
    table_match=re.search(SAME COMMAND AS IN LINE 27, input_text)
    # As long as "table_match" exists, i.e. we regex result in a match, the loop 
    # will continue.

#########################
# Task 2: remove Exhibits
#########################
# Exhibits have the following structure
# <DOCUMENT>
# <TYPE>EX...
# ...
# </DOCUMENT>

# THE APPROACH IS THE SAME AS THE SEARCH FOR TABLES ABOVE
exhibit_match=re.search(, input_text)
while :
    # get the beginning of the exhibit
    exhibit_start_match=
    start_exhibit=
    # As the exhibits are at the end of the 10-K filing it would not be
    # necessary to include an end position. We could also drop the entire text
    # after "<TYPE>EX"
    # However, for completeness, we will define an end
    exhibit_end_match=
    end_exhibit=
    # Print the identified text to check whether the exhibit has be identified
    # correctly
    print("The text below is a exhibit!\n"+input_text[start_exhibit:end_exhibit])
    
    input_text=TO BE COMPLETED
    # Check whether there are further exhibits
    exhibit_match=re.search(SAME COMMAND AS IN LINE 65, input_text)

##########################
# Task 3: remove html code
##########################
# Alternative 1: remove html code without Beautiful Soup
text=re.sub(TO BE COMPLETED, '', input_text)
# Use a regex that searches for a "<" followed by at least one character that must not
# equal > and is completed by >.

# Alternative 2: remove html code using Beautiful Soup
html_text=BeautifulSoup(TO BE COMPLETED)
text=html_text.TO BE COMPLETED

########################
# Task 4: delete numbers
########################

# YOU MAY NEED MULTIPLE COMMANDS TO DELETE ALL NUMBERS
# Remember that you can have different formats, e.g., 1,234.56 or 0.12 or 1,234,567
text=re.sub(TO BE COMPLETED,'',text)

########################
# Task 5: delete symbols
########################
text=re.sub(TO BE COMPLETED,'',text)


# Open the output file for the pure text
output_file=open(directory+'Exercise_4_Application_Regular_Expressions_clean.txt','w',encoding="utf-8")
output_file.write(text)

# close all files
input_file.close()
output_file.close()

print("DONE")

