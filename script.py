import pdfplumber
import time
PDF_PATH = '/Users/akifislam/PycharmProjects/PlumberTest/Resources/AS  Biology (9700)/2011/9700_s11_qp_11.pdf'
PAGE_NUMBER = 11

SL_COLUMN_A = []  # For SL Input in Excels
QUES_TEXT_COLUMN_B = [] # For Question in Excels
OPTIONS_COLUMN_I_J_K_L = [] # Collecting Options
HAS_ANY_QTABLE= []
HAS_ANY_ANSWER_TABLE = []

def updateQTABLEStatus(index,status):
    if(HAS_ANY_QTABLE[index]==False):
        HAS_ANY_QTABLE[index] = status


def countSerial():
    count = 27 #Start of Page Count
    with pdfplumber.open(PDF_PATH) as pdf:
        page_all_texts = (pdf.pages[PAGE_NUMBER].extract_text())
        page_all_texts = page_all_texts
        spllited_page_all_texts = (page_all_texts.splitlines(False))
        # print(spllited_page_all_texts.count("?"))

        # Checking How Many Questions are in a Page
        for line in spllited_page_all_texts:
            # print(line)
            if(line.__contains__("?")):
                count+=1
                SL_COLUMN_A.append(count)

        # print("Question Serial : ",SL_COLUMN_A)






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

            #Graph Detection
            # if(line.__contains__("graph") or line.__contains__("diagram") ):
            #     print("\nGraph Detected\n")

            # #Table Detection
            # if(line.count("  ")>=2):
            #     print("\nTable Detected\n")

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




def getAnswerTableLocation():
    for i in range (0,len(OPTIONS_COLUMN_I_J_K_L)):
        if(OPTIONS_COLUMN_I_J_K_L[i][1].count("  ")>=1):
            HAS_ANY_ANSWER_TABLE.append(True)
        else:
            HAS_ANY_ANSWER_TABLE.append(False)



countSerial()
collectQuestions()
collectOptions()
# print(SL_COLUMN_A)
# print(QUES_TEXT_COLUMN_B)
# for option in OPTIONS_COLUMN_I_J_K_L:
#     print(option)
# for question in QUES_TEXT_COLUMN_B:
#    print(question.strip())
# print(HAS_ANY_QTABLE)
getAnswerTableLocation()

# print(OPTIONS_COLUMN_I_J_K_L)
print(HAS_ANY_ANSWER_TABLE)
