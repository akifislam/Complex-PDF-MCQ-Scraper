# Warning : If you are facing 'Cant parse' problem, then run this file with proper value.

#Enter your PC Username here
StartPage = 4 # 'N' no page theke shurte korte hole 'N-1' Dite hobe.
QusSerialCounter = 2 #'N' th Question theke shuru korte hole 'N-1' Dite hobe
pc_username = "akifislam"
desktop_folder_name="Incomplete files"
PDF_PATH = '/Users/akifislam/Desktop/Incomplete files/Physics/A level/2011/9702_s11_qp_12'

# -*- coding: utf-8 -*-

# Task 1 : Detect Graph / Picture and Add to Seperate Temporary Column
UPLOAD_LINK = 'http://moodle.mpower-social.com/converter/pix/images/'

import pdfplumber
import csv
from OOP import correct_answer_parser as ANSWER_SCRAPPER
from OOP.question_text_parser import collectQuestions
from OOP.answer_text_parser import collectOptions
from OOP.answer_table_parser import getAnswerTableLocation
from OOP.beautify_qtable import beautifyQTABLE
from OOP.qus_serial_counter import countSerial
from OOP.beautify_options import beautifyOptions
from OOP.correct_answer_parser import getCOORECTANSWERifExist



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








def searchQTABLE(ALL_TABLES,ONLY_ANS_TABLES):
    ALL_QTABLES = [item for item in ALL_TABLE_DATA[0] if item not in ANSWER_TABLE_DATA]
    # print("\n\nQTABLES are : ",ALL_QTABLES)
    return ALL_QTABLES[0]


# def beautifyQTABLE(table):


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

    QUES_TEXT_COLUMN_B = collectQuestions(PDF_PATH,PAGE_NUMBER,SL_COLUMN_A)
    OPTIONS_COLUMN_I_J_K_L = collectOptions(PDF_PATH,PAGE_NUMBER)
    HAS_ANY_ANSWER_TABLE = getAnswerTableLocation(OPTIONS_COLUMN_I_J_K_L)
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
            # print("Because Q_B[i] not exist")
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
            # print("HAS ANY TABLE PRINTING",HAS_ANY_ANSWER_TABLE)
            if(HAS_ANY_ANSWER_TABLE[i]==True):
                # print("Table Found")
                for data in ANSWER_TABLE_DATA[ans_table_iterator]:
                    # print("data: ", data)
                    if("A" in data or "B" in data or "C" in data or "D" in 'A \nB \nC \nD' in data ):
                        cur_options.append(data)
                        # print(data)
                ans_table_iterator+=1
            else:
                # print("This question has no table")
                if(len(OPTIONS_COLUMN_I_J_K_L[i])==4):
                    cur_options = [OPTIONS_COLUMN_I_J_K_L[i][0], OPTIONS_COLUMN_I_J_K_L[i][1], OPTIONS_COLUMN_I_J_K_L[i][2],OPTIONS_COLUMN_I_J_K_L[i][3]]
                else:
                    cur_options = ["Can't Parse", "Can't Parse", "Can't Parse", "Can't Parse"]

        except:
            print("Couldn't get Options because of TABLE")
        # print("ALL TABLE DATA", ALL_TABLE_DATA)
        try:
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
        except:
            print("Couldn't get Options because Options Length not 1")


        # print("OPTION SIZE : ", len(cur_options))
        # print(cur_options)


        temp_QTABLE_data = []

        # Deleting Hash from Right Side
        cur_ans_col_header_l1 = cur_ans_col_header_l1.rstrip().rstrip('#')
        cur_ans_col_header_l2 = cur_ans_col_header_l2.rstrip().rstrip('#')
        cur_ans_row_header_l2 = cur_ans_row_header_l2.rstrip().rstrip('#')


        if(isExistAnyDiagram(cur_question_text)):
            temp_graph_diagram_status = f"{UPLOAD_LINK}/{cur_qus_name}_{cur_seral}.png"
        else:
            temp_graph_diagram_status = ""
        if (len(ALL_TABLE_DATA[0]) - len(ANSWER_TABLE_DATA)) > 0:
            temp_QTABLE_data = searchQTABLE(ALL_TABLE_DATA[0], ANSWER_TABLE_DATA)

        try:
            temp_QTABLE_data = beautifyQTABLE(temp_QTABLE_data)
        except:
            temp_QTABLE_data = temp_QTABLE_data
        # print("QTABLE DATA : ", temp_QTABLE_data)

        cur_qus_correct_ans = getCOORECTANSWERifExist(cur_seral,CORRECT_MCQ_ANSWERS)
        #Error Handler
        if(len(cur_options)==4):
            writer.writerow([cur_seral,(str(cur_qus_name)+"_Q"+str(cur_seral)),cur_question_text,temp_QTABLE_data,temp_graph_diagram_status,cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[1],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[2],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[3],HAS_ANY_ANSWER_TABLE[i]),cur_qus_correct_ans])
        elif(len(cur_options)==3):
            writer.writerow([cur_seral,(str(cur_qus_name)+"_Q"+str(cur_seral)),cur_question_text,temp_QTABLE_data, temp_graph_diagram_status, cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[1],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[2],HAS_ANY_ANSWER_TABLE[i]),"Cant Parse",cur_qus_correct_ans])
        elif(len(cur_options)==2):
            writer.writerow([cur_seral,(str(cur_qus_name)+"_Q"+str(cur_seral)),cur_question_text,temp_QTABLE_data, temp_graph_diagram_status,cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),beautifyOptions(cur_options[1],HAS_ANY_ANSWER_TABLE[i]),"Cant Parse","Cant Parse",cur_qus_correct_ans])
        elif(len(cur_options)==1):
            writer.writerow([cur_seral,(str(cur_qus_name)+"_Q"+str(cur_seral)),cur_question_text,temp_QTABLE_data,temp_graph_diagram_status, cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,beautifyOptions(cur_options[0],HAS_ANY_ANSWER_TABLE[i]),"Cant Parse","Cant Parse","Cant Parse",cur_qus_correct_ans])
        elif(len(cur_options)==0):
            writer.writerow([cur_seral,(str(cur_qus_name)+"_Q"+str(cur_seral)),cur_question_text,temp_QTABLE_data,temp_graph_diagram_status, cur_Q_TABLE,cur_answer_format,cur_ans_col_header_l1,cur_ans_col_header_l2,cur_ans_row_header_l2,"Cant Parse__","Cant Parse__","Cant Parse__","Cant Parse__",cur_qus_correct_ans])
    print("Status : SUCCESS")




import glob
path = PDF_PATH
count = 0
for cur_path in glob.glob(path+"/**", recursive = True):
    NuclearBomb()
    if(str(cur_path.split('/')[-1]).__contains__("qp") and str(cur_path.split('/')[-1]).__contains__("pdf") and str(cur_path)):
        newFilePath = (str(cur_path).rstrip(str(cur_path.split('/')[-1]))) #Saving Address
        PDF_PATH = cur_path
        CSVFILENAME = str(cur_path.split('/')[-4])+"_"+str(cur_path.split('/')[-3])+"_"+str(cur_path.split('/')[-2])+"_"+str(cur_path.split('/')[-1]).rstrip(".pdf")+ "_Complete.csv"
        print("Trying to Create CSV on Directory : ",newFilePath)
        print("Creating New File :", CSVFILENAME)
        print()

        with pdfplumber.open(PDF_PATH) as pdf:
            newCSVfile = open(newFilePath+CSVFILENAME, 'w')

            writer = csv.writer(newCSVfile)
            # Adding Header
            writer.writerow(
                ['SL.', 'Question Name*', 'Question Text*', '(TEMP)Any QTABLE?', '(TEMP)Require Screenshot?',
                 'Question Table <QTABLE>', 'Answer Format*',
                 'Answer Column header/s Level1*', 'Answer Column header/s Level2', 'Answer Row header/s Level2',
                 'Option A*', 'Option B*', 'Option C*', 'Option D*', 'Correct Answer*', 'Tags-Topic', 'Tag-Difficulty*',
                 'Tag-UniqueID*', 'General Feedback', 'Grade(Default =1)', 'Penalty (default = none)',
                 'Shuffle Answers (default = no)', 'Answer numbering (default = abcd..)'])



            totalPage = len(pdf.pages)
            print("TOTAL PAGE in this DOC :" ,totalPage)
            CORRECT_MCQ_ANSWERS = ANSWER_SCRAPPER.getAnswer(PDF_PATH)

            for cur_page in range (StartPage,totalPage):
                PAGE_NUMBER = cur_page
                SL_COLUMN_A = countSerial(PDF_PATH,PAGE_NUMBER,QusSerialCounter)
                QusSerialCounter+=len(SL_COLUMN_A)

                killDataEntryExpert()

                NuclearBomb()

            newCSVfile.close()



