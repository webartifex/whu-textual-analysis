# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:21:46 2015

@author: Alexander Hillert, Goethe Uni Frankfurt
"""
import re
# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the txt file with the SEC filings
sec_filings_file=open(directory+'formidx_1998Q1.txt','r')
sec_filings_text=sec_filings_file.read()

# Create output file
output_file=open(directory+'SEC_Filings_Output.csv','w')

# Create first line with variable names
# I use semicolons as separator in csv files. You can also use any other symbol.
# However, you should make sure that the separator is not part of the data/text
# you write to the file.
# For example, it would be problematic if you use comma as separator and have
# company names like "AMERICAN HEALTHCORP, INC." or "AMERICAN FUNDING, INC."
output_file.write("Form_Type;Company_Name;CIK;Filing_Date;Link\n")

# Split the Input File in separate line
sec_filings_line=sec_filings_text.split("\n")

# Loop over all lines
for i in range(len(sec_filings_line)):
    # Does the line refer to a form 10-K file?
    # As pointed out by Loughran and McDonald (2011), many firms mislabelled
    # their 10-K filings as 10-K405 filings. Thus, I included these filings
    # as well.
    # The condition below excludes amendments to 10-Ks ("10-K/A" and "10-K405/A").
    # Depending on the research question at hand one could include amendments as well.
    # Also, 10KSB (small businesses) could also be included.
    
    match_10k=re.search("\A10-K( |405 )",sec_filings_line[i])
    if match_10k:
        
    #if sec_filings_line[i].startswith("10-K ")==1 or sec_filings_line[i].startswith("10-K405 ")==1:
        # Split the line such that the information can be saved in separate
        # variables
        # Each information item has a fixed length in the overview files of the
        # SEC.
        # Filing type: position 1 to 12
        # Remember Python starts counting at 0 and does not include the upper bound
        filing_type=sec_filings_line[i][:12]
        # Company name: position 13 to 74
        company_name=sec_filings_line[i][12:74]
        # CIK: position 75 to 86
        cik=sec_filings_line[i][74:86]
        # Filing date: position 87 to 98
        filing_date=sec_filings_line[i][86:98]
        # Link: position 99 to end of line
        link=sec_filings_line[i][98:]
        
        # Is the 10-K filed between March 10 and March 20?
        # The filing date is in the format "YYYY-MM-DD" (e.g. "1998-03-31")
        filing_day=filing_date[8:10]
        filing_month=filing_date[5:7]
        # Is the Filing Month March?
        if int(filing_month)==3 and int(filing_day)>=10 and int(filing_day)<=20:
            # The filing meets the conditions -->
            # Write output to the csv file
            output_file.write(filing_type+";"+company_name+";"+cik+";"+filing_date+";"+link+"\n")

sec_filings_file.close()
output_file.close()

print("DONE")