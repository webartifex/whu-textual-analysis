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
table_match=re.search('<TABLE>', input_text)
print("This is the result of the re.search command:")
print(table_match)
while table_match:
    # When we have identified a match, i.e. the start of a table, we save
    # the position of the beginning of the table in the variable "start_table"
    table_start_match=re.search('<TABLE>', input_text)
    start_table=table_start_match.start()
    # Next, we search for the corresponding html tag that indicates the end of
    # the table and save the end position to the variable "end_table"
    table_end_match=re.search('</TABLE>', input_text)
    end_table=table_end_match.end()
    
    # We can print the text between the start and end html tag to check whether
    # the table has been identified correctly.
    print("The text below is a table!\n"+input_text[start_table:end_table]+"\n")

    # the text between the beginning and end of the html tags is the part which
    # we would like to delete.
    # Consequently, we keep the text before the beginning of the table as well
    # as the text after the ending of the table.
    input_text=input_text[:start_table]+input_text[end_table:]
    # Next, we need to check whether there is another table in the rest of the
    # text.
    table_match=re.search('<TABLE>', input_text)
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
exhibit_match=re.search('<TYPE>EX', input_text)
while exhibit_match:
    exhibit_start_match=re.search('<TYPE>EX', input_text)
    start_exhibit=exhibit_start_match.start()
    # As the exhibits are at the end of the 10-K filing it would not be
    # necessary to include an end position. We could also drop the entire text
    # after "<TYPE>EX"
    # It is important that we search for the </DOCUMENT> only after the exhibit
    # started. Otherwise, we could get the end of the main document. 
    exhibit_end_match=re.search('</DOCUMENT>', input_text[start_exhibit:])
    end_exhibit=start_exhibit+exhibit_end_match.end()
    # Print the identified text to check whether the exhibit has be identified
    # correctly
    print("The text below is an exhibit!\n"+input_text[start_exhibit:end_exhibit]+"\n")
    
    input_text=input_text[:start_exhibit]+input_text[end_exhibit:]
    # Check whether there are further exhibits
    exhibit_match=re.search('<TYPE>EX', input_text)

##########################
# Task 3: remove html code
##########################
# Alternative 1: remove html code without Beautiful Soup
text=re.sub('<[^>]{1,}>', '', input_text)
# This regex searches for a "<" followed by at least one character that must not
# equal > and is completed by >.
# You might have thought about using the following command
#text=re.sub('<.{1,}>', '', input_text)
# However, this command has a problem, as it would delete the following line
# entirely: <page> This is some text that should remain <page>
# The .{1,} would match 'page> This is some text that should remain <page', as
# regex are greedy. The [^>]{1,} avoids this problem by not allowing to match >
# Consequently, in the example only the two "<page>" would be deleted.
# You can verify this by using regex101.com (remember to check "Python" in the
# left menu of the webpage)

# Alternative 2: remove html code using Beautiful Soup
html_text=BeautifulSoup(input_text, 'html.parser')
text=html_text.get_text()

########################
# Task 4: delete numbers
########################
# Alternative 1 - removing numbers step by step
# remove commas in numbers, e.g., 1,000 or 12,345,678 or 123,456,789,123,123
text=re.sub('[0-9]{1,3},([0-9]{3},){0,}[0-9]{3}','',text)
# remove dots in numbers, e.g., 34.56 or 12,345.678 (-> previous command leaves .678)
text=re.sub('[0-9]{0,}\.[0-9]{1,}','',text)
# remove the remaining numbers without commas and dots
text=re.sub('[0-9]','',text)

# Alternative 2 - removing numbers using a single regex
text=re.sub('[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}','',text)

# Alternative 3 - removing numbers step by step but start with commas and dots
# 1. remove comma incl. the surrounding numbers
text=re.sub("[0-9],[0-9]","",text)
# 2. remove dots incl. the surrounding numbers
text=re.sub("[0-9]\.[0-9]","",text)
# 3. remove any remaining number
text=re.sub("[0-9]","",text)


########################
# Task 5: delete symbols
########################
# When analyzing tone, symbols do not matter, as they are not considered to be
# words and thus do not biased the total word count.
# However, for training purposes this task is included in the problem.
# There is no well defined list of which symbols should be deleted. So, you
# can add further symbols.
text=re.sub('\(|\)|\[|\]|\$|§|%|\*|/|·|-',' ',text)
text=re.sub('[^a-zA-Z \.,\!\?\n]','',text)

# Open the output file for the pure text
output_file=open(directory+'Exercise_4_Application_Regular_Expressions_clean.txt','w',encoding="utf-8")
output_file.write(text)

input_file.close()
output_file.close()

print("DONE")

