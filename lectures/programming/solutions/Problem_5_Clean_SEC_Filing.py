# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:50:22 2016

@author: Alexander Hillert, Goethe University Frankfurt
"""
import re
from bs4 import BeautifulSoup

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

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
table_match=re.search('<TABLE>', input_text)
while table_match:
    # Search for the beginning of the table
    table_start_match=re.search('<TABLE>', input_text)
    start_table=table_start_match.start()
    # search for the end of the table
    table_end_match=re.search('</TABLE>', input_text)
    end_table=table_end_match.end()
    # The if condition and the printing are just for illustrative purposes.
    # The commands display the first two tables that are removed from the text.
    if i<=2:
        print("This is the "+str(i)+". Table in the 10-K.\n"+input_text[start_table:end_table]+"\n")
        i=i+1
    # remove the table
    input_text=input_text[:start_table]+input_text[end_table:]
    # check whether there are further tables
    table_match=re.search('<TABLE>', input_text)
    
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
exhibit_match=re.search('<TYPE>EX', input_text)
while exhibit_match:
    # Search for the beginning of the exhibit
    exhibit_start_match=re.search('<TYPE>EX', input_text)
    start_exhibit=exhibit_start_match.start()
    # Search for the end of the exhibit
    # CAUTION: search only in the text after the beginning of the exhibt, as
    # </DOCUMENT> also appears earlier (e.g. end of main document)
    exhibit_end_match=re.search('</DOCUMENT>', input_text[start_exhibit:])
    end_exhibit=start_exhibit+exhibit_end_match.end()
    if i<=1:
        print("This is the "+str(i)+". Exhibit in the 10-K.\n"+input_text[start_exhibit:end_exhibit]+"\n")
        i=i+1
    # remove exhibit
    input_text=input_text[:start_exhibit]+input_text[end_exhibit:]
    exhibit_match=re.search('<TYPE>EX', input_text)
    
##################
# Remove html code
##################
html_text=BeautifulSoup(input_text, 'html.parser')
text=html_text.get_text()

############################
# Remove the Document Header
############################
# There are different possibilities how one can define the start of the main part of the text
# In general, you should delete all text that is uninformative for your analysis.
# Alternative 1:
# Search for Table of Contents. To not mistakenly match a reference to the
# table of contents somewhere in the text, we require a linebreak before and after.
# When the "Table of Contents" is centered, there will be whitespaces or tabs
# before and potentially also after
header_match=re.search('(?i)\n[\t ]{0,}table[\t ]of[\t ]contents[\t ]{0,}\n', text)
# Alternative 2:
# Search for Documents incorporated by reference.
header_match=re.search('\n[\t ]{0,}DOCUMENTS[\t ]INCORPORATED[\t ]BY[\t ]REFERENCE[\t ]{0,}\n', text)
if header_match:
    # Drop the document header and keep only the rest of the text after the header.
    text=text[header_match.end():]

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
    print("Hallo")
# match now contains the last match
# Delete the text after the last match
text=text[:match.start()]


# Alternative 2: save the positions of all matches (more general approach)
# to use alternative 2, you have to comment out Alternative 1!
# Otherwise line 104 will create a problem when you execute Alternative 2.
list_start_matches=[]
list_end_matches=[]
for match in re.finditer('\s{2,}PART IV\s{0,}\n', text):
    print(match)
    list_start_matches.append(match.start())
    list_end_matches.append(match.end())
# Position of last match
print(list_start_matches[len(list_start_matches)-1])
print(list_end_matches[len(list_start_matches)-1])


# Alternative 3: manual coding using a loop of re.searches
# create a copy of the text that we can edit
text_check_part_IV=text
part_IV_match=re.search('\s{2,}PART IV\s{0,}\n', text_check_part_IV)
# create two lists that we can use to save the start and end positions
# of the Part IV matches
list_start_matches_v2=[]
list_end_matches_v2=[]
# variable to save the position of the last match in the overall text
end_position_previous_match=0
while part_IV_match:
    start_position_match=end_position_previous_match+part_IV_match.start()
    end_position_match=end_position_previous_match+part_IV_match.end()
    
    list_start_matches_v2.append(start_position_match)
    list_end_matches_v2.append(end_position_match)
    
    # update the information on the end of the last match
    end_position_previous_match=end_position_previous_match+part_IV_match.end()
    
    text_check_part_IV=text_check_part_IV[part_IV_match.end():]
    part_IV_match=re.search('\s{2,}PART IV\s{0,}\n', text_check_part_IV)

# when you compare list_end_matches to list_end_matches_v2, you see that the two
# approaches yield the same result.
# To double check that the approaches have the same results, you could
# replace the Regex in lines 112, 124, and 142 by "\s{2,}PART [A-Z]{1,3}\s{0,}\n".
# In these case you have more matches and so you can better check that the
# two approaches have identical outcomes.
'''

'''
# Delete the text after the last match
text=text[:list_start_matches[len(list_start_matches)-1]]
'''

# Delete item numbers
# This is optional. It removes "Item  1.", "ITEM 1.", "Item 10.", "Item  7A."
text=re.sub('(?i)Item [0-9]{1,}A{0,1}(\s|\.|:|\n)','',text)

# Delete numbers
text=re.sub('[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}','',text)

# Alternative stepwise procedure to delete numbers
# remove commas in numbers, e.g., 1,000 or 12,345,678
text=re.sub('[0-9]{1,3},([0-9]{3},){0,}[0-9]{3}','',text)
# remove dots in numbers, e.g., 34.56 or 12,345.678 (-> previous command leaves .678)
text=re.sub('[0-9]{0,}\.[0-9]{1,}','',text)
# remove the remaining numbers without commas and dots
text=re.sub('[0-9]','',text)


# Hyphens can be used to indicate that the word is continued in the next
# line. For example, "Micro-\nsoft" (\n is the line feed).
# Delete hyphens that are followed by a line feed.
text=re.sub('-\n','',text)

# Replace symbols by a whitespace.
# Extra whitespaces are not a problem.
text=re.sub('\(|\)|\[|\]|\$|§|%|\*|/|·|-',' ',text)

# Delete dots and commas that are not part of sentences, i.e. commas and dots
# that are preceded by a line break (potentially also whitespaces and tabs)
# and that are followed by are followed by a line break (again, there may
# also be whitespaces and tabs).
text=re.sub('\n[\t ]{0,}(\.|,){1,}[\t ]{0,}\n','\n',text)

# Drop single-character words
# One can argue whether one should implement this procedure. Loughran and
# McDonald argue in one of their papers in favor of it.
# To make sure that there is just one letter, we require that there is a word
# boundary (\W) before and after. We use a positive backward looking and a
# positive forward looking condition for this to assure that the word boundary
# get not deleted as well.
text=re.sub('(?<=\W)[A-Za-z](?=\W)',' ',text)
   
    
# Open the output file for the pure text
output_file=open(directory+'0000950130-98-001359_clean.txt','w',encoding='ascii',errors='ignore')
output_file.write(text)

input_file.close()
output_file.close()
print("COMPLETED.")
