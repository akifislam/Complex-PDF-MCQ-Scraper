
# -*- coding: utf-8 -*-

# Task 1 : Detect Graph / Picture and Add to Seperate Temporary Column
UPLOAD_LINK = 'http://moodle.mpower-social.com/converter/pix/'

import pdfplumber
import csv
import answerScrapper as ANSWER_SCRAPPER
import glob
import time
PDF_PATH = " "

# Adding Data

PAGE_NUMBER = 6

SL_COLUMN_A = []  # For SL Input in Excels
QUES_TEXT_COLUMN_B = [] # For Question in Excels
OPTIONS_COLUMN_I_J_K_L = [] # Collecting Options
HAS_ANY_QTABLE= []
HAS_ANY_ANSWER_TABLE = []
ALL_TABLE_DATA = []
ANSWER_TABLE_DATA = []
OPTION_TABLE_DATA = []
CORRECT_MCQ_ANSWERS = []




def clear_IMGCOUNTER():
    global IMGCOUNTER
    IMGCOUNTER=0

def isExistAnyDiagram(question):
    if(str(question).__contains__("diagram") or str(question).__contains__("graph")):
        return True
    else:
        return False



def getCOORECTANSWERifExist(ques_no):
    if(len(CORRECT_MCQ_ANSWERS)<ques_no):
        print("Can't Parse because of GetCOrrectFunction")
        return "Can't Parse"
    else:
        print(f"Answer for Question No {ques_no} is {CORRECT_MCQ_ANSWERS[ques_no-1]}")
        return CORRECT_MCQ_ANSWERS[ques_no-1]

def beautifyQTABLE(table):
    cur_table_str = ""
    for row in range(0,len(table)-1):
        for each_column in range (0,len(table[row])):
            temp_t = table[row]
            if(each_column!=len(table[row])-1):
                modified_str = temp_t[each_column].replace("\n"," ")
                cur_table_str+=modified_str + "#"
            else:
                modified_str = temp_t[each_column].replace("\n", " ")
                if(row!=len(table)):
                    cur_table_str+=modified_str+"@@\n"
                else:
                    cur_table_str+=modified_str

    #Processing Last Row of QTABLE
    lastRow = table[-1]
    new_temp_options = []
    for item in lastRow:
        new_temp_options.append(item.split("\n"))

    lastRow = new_temp_options
    # print(lastRow)

    for i in range (0,len(lastRow[0])):
        for j in range(0,len(lastRow)):
            if(j==len(lastRow)-1):
                cur_table_str += lastRow[j][i]
                continue
            cur_table_str+=lastRow[j][i]+"#"
        if i!=len(lastRow[0])-1:
            cur_table_str+="@@\n"


    return(cur_table_str)




def searchQTABLE(ALL_TABLES,ONLY_ANS_TABLES):
    ALL_QTABLES = [item for item in ALL_TABLE_DATA[0] if item not in ANSWER_TABLE_DATA]
    # print("\n\nQTABLES are : ",ALL_QTABLES)
    return ALL_QTABLES[0]


# def beautifyQTABLE(table):

def beautifyOptions(options,hasTable):
    tick = '(cid:1)'
    cross='(cid:2)'

    # print("Original Options : ",options)
    if hasTable==False:
        return options
    else:
        stringToInsert = ""
        for item in range(1,len(options)-1):
            if(str(options[item]).__contains__(tick)):
                stringToInsert += "Right " + "#"
            elif(str(options[item]).__contains__(cross)):
                stringToInsert += "Cross " + "#"
            else:
                stringToInsert += options[item] + "#"

        #Again:
        if (str(options[-1]).__contains__(tick)):
            stringToInsert += "Right"
        elif (str(options[-1]).__contains__(cross)):
            stringToInsert += "Cross"
        else:
            stringToInsert+= str(options[-1])
        # print("Value to Insert : ",stringToInsert)
        return stringToInsert


def countSerial(initialCount):
    SLCOUNTER = initialCount
    with pdfplumber.open(PDF_PATH) as pdf:
        page_all_texts = (pdf.pages[PAGE_NUMBER].extract_text())
        page_all_texts = page_all_texts
        spllited_page_all_texts = (page_all_texts.splitlines(False))
        # print(spllited_page_all_texts.count("?"))

        # Checking How Many Questions are in a Page
        for line in spllited_page_all_texts:
            # print(line)
            if(line.__contains__("?")):
                SLCOUNTER+=1
                SL_COLUMN_A.append(SLCOUNTER)

        print("For Page " + str(PAGE_NUMBER) + "\nQuestion Serial : " + str(SL_COLUMN_A)+"\n")






def collectQuestions():
    with pdfplumber.open(PDF_PATH) as pdf:
        questionSerialiterator = 0
        page_all_texts = (pdf.pages[PAGE_NUMBER].extract_text())
        page_all_texts = page_all_texts
        spllited_page_all_texts = (page_all_texts.splitlines(False))
        cur_question = ""
        gotAnswerOptions = True
        gotQTable = False
        # Checking for Questions
        for line in spllited_page_all_texts:

            # Whiteline Ignore
            if(line.isspace()):
                continue

            #Breaking Condition
            if (questionSerialiterator == len(SL_COLUMN_A)):
                break

            #Graph Detection
            # if(line.__contains__("graph") or line.__contains__("diagram") ):
            #     print("\nGraph Detected\n")

            #Table Detection
            # if(line.count("  ")>=2):
            #     print("\nTable Detected\n")

            # Logic
            if (gotAnswerOptions and line.startswith(str(SL_COLUMN_A[questionSerialiterator]))):

                cur_question+=line.lstrip(str(SL_COLUMN_A[questionSerialiterator]))+"\n"

                # print(line)
                if(line.__contains__("A  ")):
                    gotAnswerOptions = True

                    questionSerialiterator+=1
                    QUES_TEXT_COLUMN_B.append(cur_question)
                    cur_question=""

                else:
                    gotAnswerOptions = False

            elif(gotAnswerOptions==False):
                if (line.strip("").__contains__("A  ")):
                    gotAnswerOptions = True
                    questionSerialiterator += 1
                    QUES_TEXT_COLUMN_B.append(cur_question)
                    cur_question = ""
                else:
                    if (line.count("  ") >= 2 or line.isspace()):
                        continue
                    else:
                        cur_question += line + "\n"

    # print("For Page " + str(PAGE_NUMBER) +"Questions are\n" +str(QUES_TEXT_COLUMN_B))







def collectOptions():
    with pdfplumber.open(PDF_PATH) as pdf:
        questionSerialiterator = 0
        page_all_texts = (pdf.pages[PAGE_NUMBER].extract_text())
        page_all_texts = page_all_texts
        spllited_page_all_texts = (page_all_texts.splitlines(False))
        options_for_cur_question = []
        possible_options=['A  ', 'B  ', 'C  ', 'D  ']
        # Checking for Questions
        for line in spllited_page_all_texts:

            # Whiteline Ignore
            if(line.isspace()):
                continue

            # Logic
            for i in range (0,4):
                if line.__contains__(possible_options[i]):
                    optionStartIndex = line.find(possible_options[i])
                    if(i<3):
                        optionEndIndex = line.find(possible_options[i+1])
                        options_for_cur_question.append(line[optionStartIndex+3:optionEndIndex])
                    else:
                        options_for_cur_question.append(line[optionStartIndex+3:])

                if(len(options_for_cur_question)==4):
                    OPTIONS_COLUMN_I_J_K_L.append(options_for_cur_question)
                    options_for_cur_question = []


    # print("For Page " + str(PAGE_NUMBER) + "Options are\n" + str(OPTIONS_COLUMN_I_J_K_L))



def getAnswerTableLocation():
    # print(len(OPTIONS_COLUMN_I_J_K_L))
    for i in range (0,len(OPTIONS_COLUMN_I_J_K_L)):
        if(OPTIONS_COLUMN_I_J_K_L[i][1].count("  "))>=1:
            LEN = len(OPTIONS_COLUMN_I_J_K_L[i][1])
            IND = OPTIONS_COLUMN_I_J_K_L[i][1].find("  ")
            if(LEN-IND>2):
                HAS_ANY_ANSWER_TABLE.append(True)
            else:
                HAS_ANY_ANSWER_TABLE.append(False)
        else:
            HAS_ANY_ANSWER_TABLE.append(False)

    # print("For Page " + str(PAGE_NUMBER) + "Table Location\n" + str(HAS_ANY_ANSWER_TABLE))
    # print()
def getAnswerTableData():
    with pdfplumber.open(PDF_PATH) as pdf:
        # print(pdf.pages[PAGE_NUMBER].extract_tables())
        ALL_TABLE_DATA.append(pdf.pages[PAGE_NUMBER].extract_tables())
    # if(len(ALL_TABLE_DATA[0])!=len(OPTIONS_COLUMN_I_J_K_L)):
    #         # print("Q TABLE FOUND")
    # print("For Page " + str(PAGE_NUMBER) + "ALL Table Data : \n " + str(ALL_TABLE_DATA))
    # print()
    # print()



def NuclearBomb():
    SL_COLUMN_A.clear() # For SL Input in Excels
    QUES_TEXT_COLUMN_B.clear() # For Question in Excels
    OPTIONS_COLUMN_I_J_K_L.clear() # Collecting Options

    HAS_ANY_QTABLE.clear()
    HAS_ANY_ANSWER_TABLE.clear()
    ALL_TABLE_DATA.clear()
    ANSWER_TABLE_DATA.clear()
    OPTION_TABLE_DATA.clear()
    clear_IMGCOUNTER()

    # print("Correct Answer List Size : ", len(CORRECT_MCQ_ANSWERS))
    # print("Nuclear Called")
    # print("Now Count Serial : ",SL_COLUMN_A)



def killDataEntryExpert():

    collectQuestions()
    collectOptions()

    getAnswerTableLocation()
    getAnswerTableData()


    #Getting Answer Table Data
    for i in range (0,len(ALL_TABLE_DATA[0])):
        AB_counter = 0
        # print(ALL_TABLE_DATA[0][i]) #First Table
        #Now check if it is a option table
        for j in range (0,len(ALL_TABLE_DATA[0][i])):
            if ('A' in ALL_TABLE_DATA[0][i][j] or 'B' in ALL_TABLE_DATA[0][i][j] or 'C' in ALL_TABLE_DATA[0][i][j] or 'D' in ALL_TABLE_DATA[0][i][j]):
                AB_counter+=1
            if 'A \nB \nC \nD' in ALL_TABLE_DATA[0][i][j]:
                AB_counter=4

        if(AB_counter==4):
            ANSWER_TABLE_DATA.append(ALL_TABLE_DATA[0][i])





    # Getting Question Text for Column B
    ans_table_iterator = 0
    for i in range (0,len(SL_COLUMN_A)):
        cur_seral = SL_COLUMN_A[i];
        cur_qus_name = PDF_PATH.split('/')[-1].split('.')[0]


        try:
            cur_question_text = QUES_TEXT_COLUMN_B[i]
        except:
            cur_question_text = "Can't Parse"
            print("Because Q_B[i] not exist")
            # print(QUES_TEXT_COLUMN_B)

        cur_Q_TABLE = ""
        cur_ans_row_header_l2 = ""
        cur_options = []
        cur_ans_col_header_l2 = ""
        cur_ans_col_header_l1 = ""
        cur_answer_format = ""

        # HAS TABLE i mane i-th questioner option e kono TABLE ACHE KINA
        try:
            if(HAS_ANY_ANSWER_TABLE[i]==True):
                # Getting Table Format
                cur_answer_format = "With Table"

                # Check for L1 Headers
                # print("Table : ",ANSWER_TABLE_DATA[ans_table_iterator])
                if "A" not in ANSWER_TABLE_DATA[ans_table_iterator][0]:
                    for item in ANSWER_TABLE_DATA[ans_table_iterator][0]:
                        if(str(item).isspace() or item=="," or item==None):
                            continue
                        cur_ans_col_header_l1+= item + "#"

                #Deleting Unnecessary Comma from both side
                cur_ans_col_header_l1 = cur_ans_col_header_l1.lstrip(" ").strip(',')


                # print("Header Set to : ", cur_ans_col_header_l1)

                #Check for L2 Headers
                if "A" not in ANSWER_TABLE_DATA[ans_table_iterator][1] and "A \nB \nC \nD" not in ANSWER_TABLE_DATA[ans_table_iterator][1]:
                    for item in ANSWER_TABLE_DATA[ans_table_iterator][1]:
                        if (str(item).isspace() or item == "," or item == None):
                            continue
                        cur_ans_col_header_l2 += item + "#"
                cur_ans_col_header_l2 = cur_ans_col_header_l2.lstrip(" ").lstrip(',')
        except:
            # print("Couldn't load Answer Table information")
            cur_ans_col_header_l2=""
            cur_ans_col_header_l1=""
            cur_answer_format = "No Table"

        # print(ALL_TABLE_DATA)

        try:
            #Filliing Up Options
            if(HAS_ANY_ANSWER_TABLE[i]==True):
                # print("Table Found")
                for data in ANSWER_TABLE_DATA[ans_table_iterator]:
                    # print("data: ", data)
                    if("A" in data or "B" in data or "C" in data or "D" in 'A \nB \nC \nD' in data ):
                        cur_options.append(data)
                        # print(data)
                ans_table_iterator+=1
            else:
                if(len(OPTIONS_COLUMN_I_J_K_L[i])==4):
                    cur_options = [OPTIONS_COLUMN_I_J_K_L[i][0], OPTIONS_COLUMN_I_J_K_L[i][1], OPTIONS_COLUMN_I_J_K_L[i][2],OPTIONS_COLUMN_I_J_K_L[i][3]]
                else:
                    cur_options = ["Can't Parse", "Can't Parse", "Can't Parse", "Can't Parse"]

        except:
            print("Couldn't get Options")
        # print("ALL TABLE DATA", ALL_TABLE_DATA)
        if(len(cur_options)==1):
            new_temp_options = []
            for item in cur_options[0]:
                new_temp_options.append(item.split("\n"))
            # print("New : ", new_temp_options)
            cur_options = new_temp_options

            new_temp_options = []
            for ii in range (0,4):
                newlist = []
                for j in range(0,len(cur_options)):
                    newlist.append(cur_options[j][ii])
                new_temp_options.append(newlist)
            cur_options = new_temp_options


        # print("OPTION SIZE : ", len(cur_options))
        # print(cur_options)


        temp_QTABLE_data = []

        # Deleting Hash from Right Side
        cur_ans_col_header_l1 = cur_ans_col_header_l1.rstrip().rstrip('#')
        cur_ans_col_header_l2 = cur_ans_col_header_l2.rstrip().rstrip('#')
        cur_ans_row_header_l2 = cur_ans_row_header_l2.rstrip().rstrip('#')

        if(isExistAnyDiagram(cur_question_text)):
            temp_graph_diagram_status = f"{UPLOAD_LINK}{cur_qus_name}_{cur_seral}"
        else:
            temp_graph_diagram_status = ""
        if (len(ALL_TABLE_DATA[0]) - len(ANSWER_TABLE_DATA)) > 0:
            temp_QTABLE_data = searchQTABLE(ALL_TABLE_DATA[0], ANSWER_TABLE_DATA)

        try:
            temp_QTABLE_data = beautifyQTABLE(temp_QTABLE_data)
        except:
            temp_QTABLE_data = temp_QTABLE_data

        cur_qus_correct_ans = getCOORECTANSWERifExist(cur_seral)
        #Error Handler
        if(len(cur_options)==4):
            writer.writerow([cur_seral,cur_qus_name,cur_question_text,temp_QTABLE_data,temp_graph_diagram_status,cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[1],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[2],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[3],HAS_ANY_ANSWER_TABLE[i]),cur_qus_correct_ans])
        elif(len(cur_options)==3):
            writer.writerow([cur_seral,cur_qus_name,cur_question_text,temp_QTABLE_data, temp_graph_diagram_status, cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[1],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[2],HAS_ANY_ANSWER_TABLE[i]),"Cant Parse",cur_qus_correct_ans])
        elif(len(cur_options)==2):
            writer.writerow([cur_seral,cur_qus_name,cur_question_text,temp_QTABLE_data, temp_graph_diagram_status,cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[1],HAS_ANY_ANSWER_TABLE[i]),"Cant Parse","Cant Parse",cur_qus_correct_ans])
        elif(len(cur_options)==1):
            writer.writerow([cur_seral,cur_qus_name,cur_question_text,temp_QTABLE_data,temp_graph_diagram_status, cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),"Cant Parse","Cant Parse","Cant Parse",cur_qus_correct_ans])
        elif(len(cur_options)==0):
            writer.writerow([cur_seral,cur_qus_name,cur_question_text,temp_QTABLE_data,temp_graph_diagram_status, cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,"Cant Parse","Cant Parse","Cant Parse","Cant Parse",cur_qus_correct_ans])
    print("Status : SUCCESS")



import glob
path = '/Users/akifislam/Desktop/QuestionReader/AS  Biology (9700)'
count = 0
for cur_path in glob.glob(path+"/**", recursive = True):
    NuclearBomb()
    if(str(cur_path[-18:]).__contains__("qp") and str(cur_path[-18:]).__contains__(".pdf")):
        PDF_PATH = cur_path
        CSVFILENAME = cur_path[-18:] + "_CompleteInput.csv"
        print("Trying to Create CSV on Directory : ", cur_path[0:63])
        print("Creating New File :", CSVFILENAME)

        with pdfplumber.open(PDF_PATH) as pdf:
            newCSVfile = open(cur_path[0:64]+'Tested/'+CSVFILENAME, 'w')

            writer = csv.writer(newCSVfile)
            # Adding Header
            writer.writerow(
                ['SL.', 'Question Name*', 'Question Text*', '(TEMP)Any QTABLE?', '(TEMP)Require Screenshot?',
                 'Question Table <QTABLE>', 'Answer Format*',
                 'Answer Column header/s Level1*', 'Answer Column header/s Level2', 'Answer Row header/s Level2',
                 'Option A*', 'Option B*', 'Option C*', 'Option D*', 'Correct Answer*', 'Tags-Topic', 'Tag-Difficulty*',
                 'Tag-UniqueID*', 'General Feedback', 'Grade(Default =1)', 'Penalty (default = none)',
                 'Shuffle Answers (default = no)', 'Answer numbering (default = abcd..)'])


            QusSerialCounter = 0
            totalPage = len(pdf.pages)
            print("TOTAL PAGE in this DOC :" ,totalPage)
            CORRECT_MCQ_ANSWERS = ANSWER_SCRAPPER.getAnswer(PDF_PATH)

            for cur_page in range (1,totalPage):
                PAGE_NUMBER = cur_page
                countSerial(QusSerialCounter)
                QusSerialCounter+=len(SL_COLUMN_A)
                try:
                    killDataEntryExpert()
                except:
                    print("Couldn't Parse")
                NuclearBomb()
                print("===========")
            newCSVfile.close()



