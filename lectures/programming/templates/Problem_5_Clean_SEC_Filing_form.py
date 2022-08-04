# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:50:22 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""
import re
from bs4 import BeautifulSoup

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"
# It is important to use a single forward slash / but not a single backslash \.
# For MAC users: your directory will usually start with "/Users/". For example:
#directory="/Users/FirstnameLastname/Textual Analysis/Programming/Files/"

# Open the 10-K
input_file=open(directory+'0000950130-98-001359.txt','r',encoding='ascii',errors='ignore')
input_text=input_file.read()

################################
# Remove tables
# Same approach as in Problem 4
################################
# Sometimes it is helpful to print the text parts that are deleted. In this
# example, we will print the first two tables that we delete.
i=1
table_match=re.search(ENTER THE REGEX, input_text)
while table_match:
    # Search for the beginning of the table
    table_start_match=re.search(REGEX FOR BEGINNING OF TABLE, input_text)
    start_table=
    # search for the end of the table
    table_end_match=REGEX FOR END OF TABLE
    end_table=
    # The if condition and the printing are just for illustrative purposes.
    # The commands display the first two tables that are removed from the text.
    if i<=2:
        print("This is the "+str(i)+". Table in the 10-K.\n"+input_text[start_table:end_table]+"\n")
        i=i+1
    # remove the table from the original text
    input_text=TO BE COMPLETED
    # check whether there are further tables
    # same command as in line 24
    table_match=re.search(XXXXXXX, input_text)
    
################################
# Remove exhibits
# Same approach as in Problem 4
################################
# Exhibits have the following structure
# <DOCUMENT>
# <TYPE>EX...
# ...
# </DOCUMENT>
# Sometimes it is helpful to print the text parts that are deleted. In this
# example, we will print the first exhibit that we delete.
i=1
exhibit_match=re.search(ENTER THE REGEX, input_text)
while exhibit_match:
    # Search for the beginning of the exhibit
    exhibit_start_match=re.search(REGEX FOR BEGINNING OF EXHIBIT, input_text)
    start_exhibit=
    # Search for the end of the exhibit
    # CAUTION: search only in the text after the beginning of the exhibt, as
    # the end-term also appears earlier (e.g. end of main document)
    exhibit_end_match=re.search(REGEX FOR END OF EXHIBIT, input_text[START OF EHIBIT UNTIL END OF TEXT])
    end_exhibit=
    if i<=1:
        print("This is the "+str(i)+". Exhibit in the 10-K.\n"+input_text[start_exhibit:end_exhibit]+"\n")
        i=i+1
    # remove exhibit from the original text
    input_text=
    # check whether there are further exhibits
    # same command as in line 55
    exhibit_match=re.search(XXXXXXX, input_text)
    
##################
# Remove html code
##################
# you can use BeautifulSoup for simplicity
html_text=BeautifulSoup(input_text, 'html.parser')
text=html_text.get_text()

############################
# Remove the Document Header
############################
# There are different possibilities how one can define the start of the main part of the text
# In general, you should delete all text that is uninformative for your analysis.
header_match=re.search(END OF DOCUMENT HEADER, text)
if header_match:
    # Drop the document header and keep only the rest of the text after the header.
    text=text[XXXXXXXXXXXXXXX]


#################################################
# Delete the text in "PART IV"
# This procedure is optional. Look at "Part IV" and decide whether you favor
# the approach. I think that the part should be dropped, as it is just a list
# of exhibits, some mandatory text required by the SEC [indicated by the
# capital letters in the "SIGNATURES" section].
#################################################
'''
# Alternative 1: go over all matches but keep only the last one
for match in re.finditer('\s{2,}PART IV\s{0,}\n', text):
    pass
# match now contains the last match.
# Delete the text after the last match
text=text[:match.start()]

# Alternative 2: save the positions of all matches (more general approach)
list_start_matches=[]
list_end_matches=[]
for match in re.finditer('\s{2,}PART IV\s{0,}\n', text):
    list_start_matches.append(match.start())
    list_end_matches.append(match.end())
# Position of last match
print(list_start_matches[len(list_start_matches)-1])
print(list_end_matches[len(list_start_matches)-1])

# Delete the text after the last match
text=text[:list_start_matches[len(list_start_matches)-1]]
'''

# Delete item numbers
# This is optional. It removes "Item  1.", "ITEM 1.", "Item 10.", "Item  7A."
text=re.sub(TO BE COMPLETED,'',text)

# Delete numbers
# You can use the code from Problem 4.
text=re.sub(TO BE COMPLETED,'',text)


# Hyphens can be used to indicate that the word is continued in the next
# line. For example, "Micro-\nsoft" (\n is the line feed).
# Delete hyphens that are followed by a line feed.
text=re.sub(TO BE COMPLETED,'',text)

# Delete symbols
# You can use the code from Problem 4.
text=re.sub(TO BE COMPLETED,'',text)

# Delete dots and commas that are not part of sentences, i.e. commas and dots
# that are preceded by whitespace or line break and that are followed by
# whitespace or line break.
text=re.sub('\n(\.|,)\n','\n',text)

# Drop single-character words
# One can argue whether one should implement this procedure. Loughran and
# McDonald argue in one of their papers in favor of it.
# To make sure that there is just one letter, we require that there is a word
# boundary (\W) before and after. We use a positive backward looking and a
# positive forward looking condition for this to assure that the word boundary
# get not deleted as well.
text=re.sub(TO BE COMPLETED,' ',text)
   
    
# Open the output file for the pure text
output_file=open(directory+'0000950130-98-001359_clean.txt','w',encoding='ascii',errors='ignore')
output_file.write(text)

input_file.close()
output_file.close()
print("COMPLETED.")

