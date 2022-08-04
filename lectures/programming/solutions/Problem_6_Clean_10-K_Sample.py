# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe University Frankfurt
"""

import re
from bs4 import BeautifulSoup

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r')
input_text=input_file.read()

# Split the input file in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the iput file. The following command
# deletes these lines
while input_text_line.count("")>0:
    input_text_line.remove("")

print("The input file contains "+str(len(input_text_line)-1)+" non-empty lines with data.")
# We subtract 1 from the lenght, as the first line contains the variable names but not data.

# Loop over all lines
for i in range(1,len(input_text_line)):
    # To see the progress of your program you can print the number of iteration.
    print(str(i))
    
    # split the lines of the CSV-file into the two variables
    variables=input_text_line[i].split(";")
    # We need the CIK and the filename to open the file
    cik=variables[0]
    filename=variables[1]
    
    # Open the ith 10-K in the list
    input_file_10_k=open(directory+'10-K_Sample/'+cik+'_'+filename,'r',encoding='ascii',errors='ignore')
    input_text_10_k=input_file_10_k.read()
    
    # the new file name should be "old_name_clean" -> we have to replace ".txt"
    # by "_clean.txt"
    filename=filename.replace('.txt','_clean.txt')
    
    # Remove tables
    variable=re.search('<TABLE>', input_text_10_k)
    while variable:
        variable=re.search('<TABLE>', input_text_10_k)
        start_table=variable.start()
        variable=re.search('</TABLE>', input_text_10_k)
        end_table=variable.end()
        input_text_10_k=input_text_10_k[:(start_table)]+input_text_10_k[(end_table):]
        variable=re.search('<TABLE>', input_text_10_k)
    
    
    ####################### Begin of exhibits removal #########################
    # Exhibits have the following structure
    # <DOCUMENT>
    # <TYPE>EX...
    # ...
    # </DOCUMENT>
    # In the recent years, there are also exhibits with <TYPE>EXCEL
    # -> as we search for "<TYPE>EX", the loop will delete <TYPE>EXCEL exhibits, too.
    variable=re.search('<TYPE>EX', input_text_10_k)
    while variable:
        variable=re.search('<TYPE>EX', input_text_10_k)
        start_exhibit=variable.start()
        variable=re.search('</DOCUMENT>', input_text_10_k[start_exhibit:])
        end_exhibit=start_exhibit+variable.end()
        input_text_10_k=input_text_10_k[:(start_exhibit)]+input_text_10_k[(end_exhibit):]
        variable=re.search('<TYPE>EX', input_text_10_k)
        
    # In recent years, there are also XML-Exibits.
    # CAUTION: These are <TYPE>XML and not <TYPE>EX -> need separate cleaning
    # Remove XML-Exhibits, which have the following structure
    # <DOCUMENT>
    # <TYPE>XML
    # ...
    # </DOCUMENT>
    variable=re.search('<TYPE>XML', input_text_10_k)
    while variable:
        variable=re.search('<TYPE>XML', input_text_10_k)
        start_exhibit=variable.start()
        variable=re.search('</DOCUMENT>', input_text_10_k[start_exhibit:])
        end_exhibit=start_exhibit+variable.end()
        input_text_10_k=input_text_10_k[:start_exhibit]+input_text_10_k[end_exhibit:]
        variable=re.search('<TYPE>XML', input_text_10_k)
    
    # Furthermore, also in recent years, there are also ZIP-Exibits.
    # CAUTION: These are <TYPE>ZIP and not <TYPE>EX -> need separate cleaning
    # Remove ZIP-Exhibits, which have the following structure
    # <DOCUMENT>
    # <TYPE>ZIP
    # ...
    # </DOCUMENT>
    variable=re.search('<TYPE>ZIP', input_text_10_k)
    while variable:
        variable=re.search('<TYPE>ZIP', input_text_10_k)
        start_exhibit=variable.start()
        variable=re.search('</DOCUMENT>', input_text_10_k[start_exhibit:])
        end_exhibit=start_exhibit+variable.end()
        input_text_10_k=input_text_10_k[:start_exhibit]+input_text_10_k[end_exhibit:]
        variable=re.search('<TYPE>ZIP', input_text_10_k)
    
    # In addition, there are many Graphic-Exibits.
    # CAUTION: These are <TYPE>GRAPHIC and not <TYPE>EX -> need separate cleaning
    # Remove GRAPHIC-Exhibits, which have the following structure
    # <DOCUMENT>
    # <TYPE>GRAPHIC
    # ...
    # </DOCUMENT>
    variable=re.search('<TYPE>GRAPHIC', input_text_10_k)
    while variable:
        variable=re.search('<TYPE>GRAPHIC', input_text_10_k)
        start_exhibit=variable.start()
        variable=re.search('</DOCUMENT>', input_text_10_k[start_exhibit:])
        end_exhibit=start_exhibit+variable.end()
        input_text_10_k=input_text_10_k[:start_exhibit]+input_text_10_k[end_exhibit:]
        variable=re.search('<TYPE>GRAPHIC', input_text_10_k)
        
    # Furthermore, there can be also Cover-Exibits.
    # CAUTION: These are <TYPE>COVER and not <TYPE>EX -> need separate cleaning
    # Remove COVER-Exhibits, which have the following structure
    # <DOCUMENT>
    # <TYPE>COVER
    # ...
    # </DOCUMENT>
    variable=re.search('<TYPE>COVER', input_text_10_k)
    while variable:
        variable=re.search('<TYPE>COVER', input_text_10_k)
        start_exhibit=variable.start()
        variable=re.search('</DOCUMENT>', input_text_10_k[start_exhibit:])
        end_exhibit=start_exhibit+variable.end()
        input_text_10_k=input_text_10_k[:start_exhibit]+input_text_10_k[end_exhibit:]
        variable=re.search('<TYPE>COVER', input_text_10_k)

	# Furthermore, there can be also PDF files attached.
	# These attachments caused BeautifulSoup to crash on some computers.
    # Remove PDFs
    variable=re.search('<PDF>', input_text_10_k)
    while variable:
        variable=re.search('<PDF>', input_text_10_k)
        start_pdf=variable.start()
        variable=re.search('</PDF>', input_text_10_k[start_pdf:])
        end_pdf=start_pdf+variable.end()
        input_text_10_k=input_text_10_k[:(start_pdf)]+input_text_10_k[(end_pdf):]
        variable=re.search('<PDF>', input_text_10_k)
	
    ######################## End of exhibits removal ##########################
    
    # Remove Document Header - PART 1
    # This condition should work for all 10-K filings as the hmtl tags "<SEC-HEADER>"
    # and "</SEC-HEADER>" are mandatory for all filings.
    variable=re.search('</SEC-HEADER>', input_text_10_k)
    if variable:
        input_text_10_k=input_text_10_k[variable.end():]
    
    
    # In some filings, firms do not use line feeds \n but <div> and </div>
    # instead to indicate the start and the end of sentences.
    # "Dieses allgemeine Element bewirkt nichts weiter als dass es in einer 
    # neuen Zeile des Fließtextes beginnt."
    # see https://wiki.selfhtml.org/wiki/HTML/Textstrukturierung/div
    # and
    # "The <div> tag defines a division or a section in an HTML document.
    # By default, browsers always place a line break before and after the <div> element."
    # See: https://www.w3schools.com/tags/tag_div.asp
    # It is important to replace <div> and </div> by linefeeds because otherwise
    # the entire text will be in a single line and the subsequent commands do
    # not work properly.
    input_text_10_k=input_text_10_k.replace("<div>", "\n")
    input_text_10_k=input_text_10_k.replace("</div>", "\n")

    
    # Remove html code
    html_text=BeautifulSoup(input_text_10_k, 'html.parser')
    text=html_text.get_text()
    
    
    # To get an idea of what the commands below are doing, it is helpful to
    # write the current version of the text to a file and then compare it to the
    # final file.
    filename2=filename.replace('_clean.txt','_without_HtmlTablesExhibits.txt')
    # Open the output file for the text without html code and without tables+exhibits
    output_file_10_k=open(directory+'10-K_Sample/'+cik+'_'+filename2,'w',encoding='ascii',errors='ignore')
    output_file_10_k.write(text)
    output_file_10_k.close()
    
    
    # Remove the Document Header - PART II
    # The above command to remove the header ("</SEC-HEADER>") does not capture
    # the entire header -> we need to delete further parts at the top the filing.
    # WARNING: The filters below may be specific to this sample of 10-Ks.
    # Some firms have line breaks instead of whitespaces -> use "[ \n]" and not just " ".
    variable=re.search('(?i)\n {0,}DOCUMENTS[ \n]INCORPORATED[ \n]BY[ \n]REFERENCE {0,}\n', text)
    if variable:
        text=text[variable.end():]
    else:
        variable=re.search('(?i)\n {0,}table of contents {0,}\n', text)
        if variable:
            text=text[variable.end():]
        else:
            variable=re.search('(?i)\n {0,}Indicate the number of shares outstanding\.{1,}', text)
            if variable:
                text=text[variable.end():]
            else:
                variable=re.search('(?i)may be deemed “forwardlooking statements”\.{1,}', text)
                if variable:
                    text=text[variable.end():]
                else:
                    variable=re.search('\nPART\.{1,}', text)
                    if variable:
                        text=text[variable.end():]
    
    
    # Delete Item numbers
    text=re.sub('(?i)Item {1,}[0-9]{1,}(A|B){0,1}(\s|\.|:|\n)','',text)
    # Delete Part numbers
    text=re.sub('(?i)Part (1|2|3|4|III|II|I|IV)','',text)
    
    # Delete numbers:
    text=re.sub('[0-9]{1,}(,[0-9]{3}){0,}(\.[0-9]{1,}){0,1}','',text)
    
    # File names, e.g. exhibit.pdf or picture.jpeg should be removed
    text=re.sub("[ |\n]\S{1,}\.(pdf|htm|html|doc|jpg|txt|xml)(?=[ \n\.\?!])", "", text)
    
    # URLs --> Remove internet addresse
    text=re.sub("http:/{0,2}", "", text)
    text=re.sub("www\..{1,}\.[a-z]{2,4}(?=[ \n\.\?!])", "", text)
    
    
    # In Part 4 of the programming chapter, we will determine the number of
    # words per sentence. To be able to use the same underlying sample,
    # we need to implement further corrections. These changes do not affect
    # the percentage of negative/positive/etc. words.
    # --> Only relevant for determining the number of sentences
    # The text contains dots that do not indicate the end of a sentence.
    # E.g., "Inc." and "St."
    # The preceding - is found in non-U.S. for example.
    # Replace or remove specific abreviations
    # This list is incomplete. In a research project you should spend more time
    # on editing the data.
    text=re.sub("(?i)(-|\s|\A|,)Inc\.", " Inc", text)
    text=re.sub("(?i)(-|\s|\A|,)Corp\.", " Corp", text)
    text=re.sub("(?i)(-|\s|\A|,)Ltd\.", " Ltd", text)
    text=re.sub("(?i)(-|\s|\A|,)Co\.", " Co", text)
    text=re.sub("(?i)(-|\s|\A|,)S\.A\.", " SA", text)
    text=re.sub("(?i)(-|\s|\A|,)U\.S\.", " US", text)
    text=re.sub("(?i)(-|\s|\A|,)Ms\.", " Ms", text)
    text=re.sub("(?i)(-|\s|\A|,)Mr\.", " Mr", text)
    text=re.sub("(?i)(-|\s|\A|,)No\.", " Number", text)
    text=re.sub("(?i)(-|\s|\A|,)v\.s\.", " vs", text)
    text=re.sub("(?i)(-|\s|\A|,)St\.", " ", text)
    text=re.sub("(?i)(-|\s|\A|,)Jr\.", " ", text)
    
    text=re.sub("(?i)(\s|\A|,)Jan\.", " January", text)
    text=re.sub("(?i)(\s|\A|,)Feb\.", " February", text)
    text=re.sub("(?i)(\s|\A|,)Mar\.", " March", text)
    text=re.sub("(?i)(\s|\A|,)Apr\.", " April", text)
    text=re.sub("(?i)(\s|\A|,)May\.", " May", text)
    text=re.sub("(?i)(\s|\A|,)Jun\.", " June", text)
    text=re.sub("(?i)(\s|\A|,)Jul\.", " July", text)
    text=re.sub("(?i)(\s|\A|,)Aug\.", " August", text)
    text=re.sub("(?i)(\s|\A|,)Sep\.", " September", text)
    text=re.sub("(?i)(\s|\A|,)Oct\.", " October", text)
    text=re.sub("(?i)(\s|\A|,)Nov\.", " November", text)
    text=re.sub("(?i)(\s|\A|,)Dec\.", " December", text)
        
    # The sequence capital letter -> dot -> capital letter -> dot indicates an abbreviation
    # three repitions of capital letter and dot are also common in filings
    # we need to check for three instances first.
    text=re.sub("( |\n|,)[A-Z]\.[A-Z]\.[A-Z]\.", " ", text)
    # now check for two instances
    text=re.sub("( |\n|,)[A-Z]\.[A-Z]\.", " ", text)
    
    # Dots after a single letter can indicate a middle Name Paul J. Smith
    # or an abbreviation --> also delete these. 
    text=re.sub("( |\n|,)[A-Z]\.", "", text)
    
    
    # Hyphens can be used to indicate that the word is continued in the next
    # line. For example, "Micro-\nsoft" (\n is the line feed).
    # Replace hyphens followed by a line feed by a hyphen without line feed
    text=re.sub('-\n','-',text)
    
    # Delete the minus/hyphens
    # "Short-term" -> "shortterm"
    text=re.sub('-','',text)
    
    
    # --> Only relevant for determining the number of sentences
    # Delete dots and commas that are not part of sentences, i.e. commas and dots
    # that are preceded by whitespace or line break and that are followed by
    # whitespace or line break.
    text=re.sub('\n(\.|,)\n','\n',text)
    text=re.sub(' (\.|,) ',' ',text)

    # Delete single character words
    # One can argue whether one should implement this procedure. Loughran and
    # McDonald argue in one of their papers in favor of it.
    # To make sure that there is just one letter, we require that there is a word
    # boundary (\W) before and after. We use a positive backward looking and a
    # positive forward looking condition for this to assure that the word boundary
    # get not deleted as well.
    text=re.sub('(?i)(?<=\W)[a-z](?=\W)',' ',text)
    
    
    # There are sentences that are in upper case letters. However, these are not
    # "real" sentences. Examples: "RESTRICTIONS ON TRANSFER OF NOTE."
    # or "THIS NOTE AND THE RIGHTS AND OBLIGATIONS EVIDENCED HEREBY ARE
    # SUBORDINATED TO THE PRIOR PAYMENT OF CERTAIN OBLIGATIONS [...]"
    # We save the edited text in a new variable
    text_edited=text
    # Split text in sentences
    list_sentences=re.split('\.|!|\?', text)
    # iterate the list of all sentences
    for j in range(0,len(list_sentences)):
        # Determine the number of upper case letters
        upper_letters=len(re.findall('[A-Z]',list_sentences[j]))
        # Determine the number of all letters
        total_letters=len(re.findall('[A-Za-z]',list_sentences[j]))
        # If there is at least one letter calculate the fraction of upper case letters
        if total_letters>0:
            ratio=upper_letters/total_letters
            # If the fraction of upper case letters is larger than 0.9 delete
            # the sentence from the text.
            if ratio>0.9:
                text_edited=text_edited.replace(list_sentences[j]+'.','')
                text_edited=text_edited.replace(list_sentences[j]+'!','')
                text_edited=text_edited.replace(list_sentences[j]+'?','')
    
    
    # --> Only relevant for determining the number of sentences
    # There are a few cases where a dot follows a dot or where a linefeed 
    # separates two dots. --> delete the second dot.
    text_edited=text_edited.replace('..','.')
    text_edited=text_edited.replace('.\n.','.')
    
    # The following commands do not influence the subsequent textual analysis.
    # The only purpose is to display the output in a nicer format.
    # Replace lines that contain only whitespaces by a line feed.
    text_edited=re.sub('\n {1,}\n','\n',text_edited)
    
    # Replace multiple line feeds by one line feed.
    text_edited=re.sub('\n{2,}','\n',text_edited)
    
    
    # Open the output file for the pure text
    output_file_10_k=open(directory+'10-K_Sample/'+cik+'_'+filename,'w',encoding='ascii',errors='ignore')
    output_file_10_k.write(text_edited)
    output_file_10_k.close()
    input_file_10_k.close()

input_file.close()