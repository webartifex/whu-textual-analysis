# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 15:20:32 2022

@author: Alexander Hillert, Goethe University
"""

# import packages
import re

# define working directory
# adjust it to your computer
directory = "YOUR DIRECTORY"


# =============================================================================
# Part A: Creating an Overview File on the Call Participants
# =============================================================================

# Create output file
output_csv_file=open(directory+'Problem_1_Overview_Calls.csv','w',encoding="utf-8")
# Write variable names to the first line of the output file
# 1) Call-ID
# 2) Filename
# 3) Fiscal Quarter
# 4) Fiscal Year
# 5) Date of the call in the format YYYYMMDD
# 6) Time of the call, e.g., 05:00 PM GMT
# 7) number of non-corporate call participants
# 8) the names of all corporate participants and their positions -> each item 
#    should be written in a seperate column
output_csv_file.write('ID;Filename;Fiscal_Quarter;Fiscal_Year;Date;Time;\
#Analysts')
# There can be up to 4 corporate particiapnts
for i in range(1,5):
    output_csv_file.write(';Name_'+str(i)+';Position_'+str(i))
output_csv_file.write('\n')

# Open the overfiew file "Overview_File_Problem_1.csv" to call the earnings calls
overview_file=open(directory+'Overview_File_Problem_1.csv','r',encoding="utf-8")
overview_text=overview_file.read()
list_earnings_calls=overview_text.split("\n")
# The last line is empty -> drop it
while list_earnings_calls.count("")>0:
    list_earnings_calls.remove("")



# iterate all earnings conference calls
for i in range(1, len(list_earnings_calls)):
    
    # reset the variables
    fiscal_quarter=""
    fiscal_year=""
    date=""
    time=""
    
    # we split the entire transcripts into three parts
    # its header
    header_text=""
    # the list of non-corporate participants
    participants_text=""
    # the list of corporate participants
    corporates_text=""
    
    # the number of analysts joining the call
    number_analysts=0
    
    # variables for manager name and position
    manager_name=""
    manager_position=""
    manager_position_edited=""
    
    # a list of manager names for part b)
    manager_name_list=[]
    
    # get the filename of each earnings call
    call_information=list_earnings_calls[i].split(";")
    call_id=call_information[0]
    filename=call_information[1]
    
    # open the call transcript
    call_file=open(directory+'Problem_1_Sample/'+filename,'r',encoding="utf-8")
    call_text=call_file.read()
    
    # Get information on the call
    # FOr example:
    # Q1 2013 Bank of America Corporation Earnings Conference Call
    # 04/17/2013 08:30 AM GMT
    
    # the header ends where the list of corporate particpants starts
    match_corporates=re.search(TO BE COMPLETED,call_text)
    if match_corporates:
        header_text=call_text[TO BE COMPLETED]

    
    # get the fiscal quarter and year from the header text
    match_fiscal_quarter=re.search(TO BE COMPLETED,header_text)
    if match_fiscal_quarter:
        fiscal_quarter=match_fiscal_quarter.group(0)
    match_fiscal_year=re.search(TO BE COMPLETED,header_text)
    if match_fiscal_year:
        fiscal_year=match_fiscal_year.group(0)

    # get date and time of the call
    # date
    match_date=re.search(TO BE COMPLETED,header_text)
    if match_date:
        date=match_date.group(0)
        # the date in the output file should be formatted as YYYYMMDD
        # so, you need to rearrange the date text
        year=date[TO BE COMPLETED]
        month=date[TO BE COMPLETED]
        day=date[TO BE COMPLETED]
        date_formatted=year+month+day
    # time
    match_time=re.search(TO BE COMPLETED,header_text)
    if match_time:
        time=match_time.group(0)
    
    
    # count the number of analysts
    # the relevant text part starts with, for example,
    # ================================================================================
    # Conference Call Participiants
    # ================================================================================
    # 
    # * Chris Mutascio
    #   Keefe, Bruyette & Woods - Analyst
    # * Thomas Laturneau
    #   FBR - Analyst
    
    # and ends with the beginning of the presentation
    # ================================================================================
    # Presentation
    # --------------------------------------------------------------------------------
    
    match_participants=re.search(TO BE COMPLETED,call_text)
    match_presentation=re.search(TO BE COMPLETED,call_text)
    # if you find both boundaries
    if match_participants and match_presentation:
        # get the text in between
        participants_text=call_text[TO BE COMPLETED]
    
    # split the text of the participants that you have just identified
    # in a way that each element refers to one analyst.
    analyst_list=participants_text.split(TO BE COMPLETED)
    # depending on how you split, you might need re.split()
    
    # check whether you get empty elements and/or elements that do not refer
    # to analysts -> remove them
    while TO BE COMPLETED>0:
        TO BE COMPLETED
        
    # after these steps and checks, the number of analysts is the length of your analyst list
    number_analysts=TO BE COMPLETED
    
    
    # get the names of the corporate participants and their position
    # remember that you already have the beginning of corporate participants
    # see above at around line 90
    # the corporate participants come before the list of non-corporate participants
    corporates_text=call_text[TO BE COMPLETED]
    # like before, split this text such that one element refers to one corporate participant
    corporates_list=corporates_text.split(TO BE COMPLETED)
    # check whether you get empty elements and/or elements that do not refer
    # to corporate participants -> remove them
    while TO BE COMPLETED>0:
        TO BE COMPLETED

        
    # write the call information to the output file
    output_csv_file.write(str(call_id)+";"+filename+";"+fiscal_quarter+";"+fiscal_year+";"\
                          +date_formatted+";"+time+";"+str(number_analysts))    
    
    # now, we need to add the information on the corporate participants
    # go over all corporate participants
    for j in range(len(corporates_list)):
        # depending on how you split the text of corporate participants,
        # one element of your list could contain the name of the mangager in the first
        # line and their position in the second line.
        # ADJUST THE FOLLOWING COMMANDS IF YOU USED A DIFFERENT SPLIT.
        
        # split each element of the list of corporate participants further 
        # into name and position
        manager_entry=corporates_list[j]
        manager_entry_parts=manager_entry.split(TO BE COMPLETED)
        manager_name=manager_entry_parts[TO BE COMPLETED]
        
        # for part b) of the problem it is helpful to have a list of all
        # manager names. With this list, we can identify whether a statement
        # comes from a managers (-> answer) or from an analyst (-> question)
        manager_name_list.append(manager_name)
        
        
        manager_position=manager_entry_parts[TO BE COMPLETED]
        # Like before, the template assumes a very specific type of split here
        # So depending on your approach, you might need to change the commands below.
        # the position is just the text part after " - "
        # For example
        # Bank of America Corporation - CEO
        # the position is "CEO"
        manager_position_edited=re.TO BE COMPLETED

        # write the manager names and positions to the output file
        output_csv_file.write(";"+manager_name+";"+manager_position_edited)
        
    output_csv_file.write("\n")   
    
    
    print("For earnings call "+str(i)+" part a) has been completed.")
    
    # =========================================================================
    # Part B: Extracting the Call Segments
    # =========================================================================
    
    # set variables
    presentation_text=""
    qanda_text=""
    qanda_list=[]
    question_text=""
    answer_text=""

    
    # identify the presentation
    # the begin of the presentation has already been identified above
    # see at around line 140
    #
    # the presentation ends where the Q and A part begins
    # ================================================================================
    # Questions and Answers
    # --------------------------------------------------------------------------------
    match_qanda=re.search(TO BE COMPLETED,call_text)
    presentation_text=call_text[TO BE COMPLETED]
    
    # drop operator statements
    # search for the beginning of an operator statement
    match_operator=re.search(TO BE COMPLETED,presentation_text)
    while match_operator:
        match_operator_start=match_operator.start()
        # search for the end of the operator statement
        # Hint: search only after the beginning of the operator statement
        # Hint 2: remember to keep track of your coordinates (.start() and .end())
        match_operator_end=re.search(TO BE COMPLETED,TO BE COMPLETED)
        
        # keep the text before the operator statement and the text after
        # the approach is similar to removing tables (see Problem 4 and 5 from class)
        presentation_text=presentation_text[TO BE COMPLETED]
        
        # check whether there is another match
        match_operator=re.search(TO BE COMPLETED,presentation_text)

    # sometimes there are technical remarks like "(inaudible)", "(corrected by company after the call)",
    # or "(technical difficulty)" -> drop those
    TO BE COMPLETED
    # there are several ways to approach this editing step (e.g., re.sub())
        
    
    # drop information on the speakers, e.g.,
    # -------------------------------------------------------------------------
    # Deborah Crawford,  Facebook, Inc. - Director of IR    [2]
    # -------------------------------------------------------------------------
    match_speaker=re.search(TO BE COMPLETED,presentation_text)
    while match_speaker:
        # the task is similar to the Operator statement but be careful
        # to only remove the speaker name but NOT the text of the speaker.
        presentation_text=presentation_text TO BE COMPLETED
        # check whether there is another speaker name
        match_speaker=re.search(TO BE COMPLETED,presentation_text)
        
    
    # write the text of the presentation to an output file
    # make sure that the folder "Problem_1_Conference_Call_Segments" exists.
    output_file_presentation=open(directory+'Problem_1_Conference_Call_Segments/call_'+str(call_id)+'_presentation.txt',"w",encoding='utf-8')
    output_file_presentation.write(presentation_text)
    
    # Close file
    output_file_presentation.close()


    # -------------------------------------------------------------------------
    # identify questions and answers
    # -------------------------------------------------------------------------
    # you already have the start of the Q&A section (see at around lines 235)
    qanda_text=call_text[match_qanda.end():]
    
    # the earnings call transcript ends with definitions
    # remove these/keep the text before the definitions
    match_definitions=re.search("\n-{1,}\nDefinitions\n-{1,}\n",qanda_text)
    if match_definitions:
        # keep the text before
        qanda_text=qanda_text[TO BE COMPLETED]
        
    # split the Q and A part by speaker
    qanda_list=re.split(TO BE COMPLETED,qanda_text)
    
    # variables to count the number of answers
    answer_counter=1
    # and questions
    question_counter=1
    
    # go over all speakers/statements that you obtained from the previous split
    # you now have to decide whether the speaker is an analyst (-> question)
    # or a corporate participant (-> answer)
    for k in range(TO BE COMPLETED):
        
        # identify the speaker name to check whether it is a corporate participant.
        # For example
        # --------------------------------------------------------------------------------
        # Bruce Thompson,  Bank of America Corporation - CFO    [3]
        # --------------------------------------------------------------------------------
        #
        speaker_text_part=qanda_list[k]
        # split the text part of the kth speaker
        # into his*her name and the rest
        # NOTE: re.search() and re.sub() are also nice ways to accomplish the goal
        speaker_text_sub_parts=re.split(TO BE COMPLETED,qanda_list[k])
        # get the name of the speaker from the previous split
        # in the example above, we need to get "Bruce Thompson"
        speaker_name=speaker_text_sub_parts[TO BE COMPLETED]
        # depending on your split, you might need some further editing to
        # get onyl the name ("Bruce Thompson") without any additional information.
        
        
        # the second part of speaker_text_sub_parts is (probably) the statement
        # of the speaker (again, it depends on your split)
        text=speaker_text_sub_parts[TO BE COMPLETED]
        
        # sometimes there are technical remarks like "(inaudible)", "(corrected by company after the call)",
        # or "(technical difficulty)" -> drop those
        text=TO BE COMPLETED
        # there are several ways to approach this editing step (e.g., re.sub())
        
        # check whether the speaker name is in the manager list from part a) (see at around line 195)
        if speaker_name in manager_name_list:
            # the name of the speaker is in the list of corporate participants
            # -> it is a management answer
            
            answer_text=answer_text+"Answer_"+str(answer_counter)+":\n"+text+"\n"
            answer_counter=answer_counter+1
            
        else:
            # it is either an analyst question or an operator statement
            # be careful to check the condition below. depending on how your
            # speaker names look like, you may need .count() and/or re.search() instead of .startswith()
            if speaker_name.startswith("Operator") or TO BE COMPLETED:
                pass

            else:
                # it is an analyst question
                question_text=question_text+"Question_"+str(question_counter)+":\n"+text+"\n"
                question_counter=question_counter+1
                         
    # write the texts to output files
    # make sure that the subfolder exists.
    output_file_answers=open(directory+'Problem_1_Conference_Call_Segments/call_'+str(call_id)+'_answers.txt',"w",encoding='utf-8')
    output_file_questions=open(directory+'Problem_1_Conference_Call_Segments/call_'+str(call_id)+'_questions.txt',"w",encoding='utf-8')
    output_file_answers.write(answer_text)
    output_file_questions.write(question_text)
    
    # Close files
    output_file_answers.close()
    output_file_questions.close()
    call_file.close() 


# Close files
overview_file.close()
output_csv_file.close()

print("Problem 1 completed.")
