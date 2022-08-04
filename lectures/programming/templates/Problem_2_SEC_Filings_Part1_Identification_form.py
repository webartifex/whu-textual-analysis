# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:21:46 2015

@author: Alexander Hillert, Goethe Uni Frankfurt
"""

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"
# It is important to use a single forward slash / but not a single backslash \.

# For MAC users: your directory will usually start with "/Users/". For example:
#directory="/Users/FirstnameLastname/Textual Analysis/Programming/Files/"

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
# DO THE LINE SPIT
sec_filings_line=

# Loop over all lines
# you can get the number of lines by computing the length of the list of lines,
# i.e. by determining the length of sec_filings_line.
for / while : # COMPLETE LOOP
    
    # Does the line refer to a form 10-K file?
    if : # USE AN IF CONDITION TO TEST THIS -> see TASKS 7 and 8 of PROBLEM 1
        
        # Split the line such that the information can be saved in separate
        # variables
        # Each information item has a fixed length in the overview files of the
        # SEC.
        # SEE SLIDE 18 FOR INFORMATION ON THE LENGTH OF THE SEPARATE COLUMNS.
        
        # COMPLETE THE COMMANDS BELOW
        filing_type=
        company_name=
        cik=
        filing_date=
        link=
        
        # Is the 10-K filed between March 10 and March 20?
        filing_day=
        filing_month=
        # Is the Filing Month March?
        if : # COMPLETE THE IF-CONDITION
            # Is the Filing Day between 10 and 20?
            if : # COMPLETE THE IF-CONDITION
                # The filing meets the conditions -->
                # Write output to the csv file
                output_file.write(filing_type+";"+company_name+";"+cik+";"+filing_date+";"+link+"\n")


# Close your input and output file in the end
sec_filings_file.close()
output_file.close()

print("DONE")