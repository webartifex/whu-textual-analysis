# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe Uni Frankfurt
"""

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# We need the urllib package
import urllib.request
# To automatically create folders we need the os-module (OS: Operating System)
import os


# Define a user agent
# Information on user agents are from https://docs.python.org/3/howto/urllib2.html:
# "Some websites dislike being browsed by programs, or send different versions
# to different browsers. By default urllib identifies itself as Python-urllib/x.y
# (where x and y are the major and minor version numbers of the Python release,
# e.g. Python-urllib/2.5), which may confuse the site, or just plain not work.
# The way a browser identifies itself is through the User-Agent header.
opener = urllib.request.build_opener()

# The SEC recently rejected requests from Python-urllib/x.y user agent (see above)
# To still automatically download files, you have different options.
# I have listed three examples below but there are many more:
# For a comprehensive list see, e.g.:
# https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/
#opener.addheaders = [('User-agent', 'Mozilla')]
#opener.addheaders = [('User-agent', 'Chrome')]
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)


# Open the csv file from part 1 of the problem
input_file=open(directory+'SEC_Filings_Output.csv','r')
input_text=input_file.read()

# Split the Input File in separate lines
input_text_line=input_text.split("\n")
# sometimes you have empty lines after a split command.
# You can remove them using the following command
while input_text_line.count("")>0:
    input_text_line.remove("")

# Create a subfolder in which the 10-K filings are saved.
# When you download a large number of filings I recommend using subfolders for
# each year or even for each year-month combination.
# The option "exist_ok=True" makes sure that you do not get an error if the
# folder already exists.
os.makedirs(directory+"10-Ks/", exist_ok=True)
    
# Loop over all lines of the csv file 
#for i in range(1,len(input_text_line)):
# To avoid having to download hundreds of files when we discuss the solution
# the loop stops at 20. (Remember the upper bound is not included.)
for i in range(1,21):
    
    # split the line into the five variables
    variables=input_text_line[i].split(";")
    # We only need the cik and the link.
    # The cik is the 3rd variable. However, the numbering of lists starts
    # at zero -> 2nd item of the list "variables"
    # The link is the 5th variable -> 4th item of the list "variables"
    cik=variables[2]
    #cik=cik.replace(" ","")
    cik=cik.strip()
    link=variables[4]
    #link=link.replace(" ","")
    link=link.strip()
    
    # Find the filename
    # The link consistes of differnt parts:
    # For example: edgar/data/1000753/0000950129-98-001035.txt
    link_parts=link.split("/")
    # 1st part: edgar
    # 2nd part: data
    # 3rd part: cik
    # 4th part: file name -> 3rd item of the set
    filename=link_parts[3]
    ###########################################################################
    ############################ WARNING ######################################
    # The filename does NOT uniquely identify the SEC filings as different firms (CIKs)
    # may use the same filename. Thus, when you only use the filename files
    # might be overwritten. To avoid this problem you need to have a unique name. 
    # Combining CIK and filename results in a unique identifier, as the 
    # filename appears only once per firm (CIK).
    # -> use the combination of CIK and filename: cik_filename
    ###########################################################################        
    urllib.request.urlretrieve("http://www.sec.gov/Archives/"+link,\
    directory+"10-Ks/"+cik+"_"+filename)
    
input_file.close()
print("DONE")