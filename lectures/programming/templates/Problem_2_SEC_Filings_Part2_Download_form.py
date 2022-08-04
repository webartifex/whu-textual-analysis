# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015

@author: Alexander Hillert, Goethe Uni Frankfurt
"""

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"
# It is important to use a single forward slash / but not a single backslash \.

# For MAC users: your directory will usually start with "/Users/". For example:
#directory="/Users/FirstnameLastname/Textual Analysis/Programming/Files/"


# We need the urllib package for the download.
import urllib.request
# To automatically create folders, we need the os-module (OS: Operating System)
import os

###############################################################################
# Technical issue
# As of March 2021, the SEC no longer accepts requests by the standard urllib settings
# you have to make some adjustments
###############################################################################
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
# END of the technical issues



# Open the csv file from part 1 of the problem
input_file=open(directory+'SEC_Filings_Output.csv','r')
input_text=input_file.read()

# Split the Input File in separate lines
input_text_line=input_text.split("\n")

# Create a subfolder in which the 10-K filings are saved.
# When you download a large number of filings I recommend using subfolders for
# each year or even for each year-month-day combination.
# In this problem, a single subfolder is fine.
os.makedirs( COMPLETE THE COMMAND )
# See slide 18 for information on the os.-commands!
# IN GENERAL, IF YOU SEE AN UNKNOWN COMMAND, GOOGLE IT TO GET INFORMATION.
    
# Loop over all lines of the csv file
# Like in part 1 of the problem, you can get the number of lines by computing
# the length of the list of lines, i.e. by determining the length of input_text_line.
for / while: # COMPLETE THE LOOP
    # split the line into the five variables
    # THE ; IS THE SEPARATOR IN THE CSV -> USE THE split() COMMAND
    variables=
    
    # We only need the cik and the link to download the file.
    # The cik is the 3rd variable.
    # The link is the 5th variable
    cik=
    link=
    
    # identify the filename
    # The link consistes of differnt parts:
    # For example: edgar/data/1000753/0000950129-98-001035.txt
    
    link_parts= # USE A SPLIT
    # 1st part: edgar
    # 2nd part: data
    # 3rd part: cik
    # 4th part: file name -> see next line
    filename=link_parts[FILE IN THE NUMBER HERE]
    ###########################################################################
    ############################ WARNING ######################################
    # The filename does NOT uniquely identify the SEC filings as different firms (CIKs)
    # may use the same filename. Thus, when you only use the filename files
    # might be overwritten. To avoid this problem you need to have a unique name. 
    # Combining CIK and filename results in a unique identifier, as the 
    # filename appears only once per firm (CIK).
    # -> use the combination of CIK and filename: cik_filename
    ###########################################################################        
    urllib.request.urlretrieve(TO BE COMPLETED)
    # See slide 19 for information on the urllib.-commands.


# Close your input file
input_file.close()

print("DONE")