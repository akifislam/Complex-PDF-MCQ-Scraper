import pdfplumber
import csv
import time
import glob


def getAnswer(question_pdf_path):
    questionYear = int((question_pdf_path.split('/')[-2]))
    if(questionYear<2017):
        # print("Working for <2017")
        #For Upto 2016
        PATH = str(question_pdf_path).replace("qp","ms")
        CORRECT_MCQ_ANSWERS = []

        with pdfplumber.open(PATH) as pdf:
            # totalPage = len(pdf.pages)
            page_all_texts = (pdf.pages[1].extract_text())
            listOfAnswers = page_all_texts.splitlines()
            #Cutting Unnecessary Values
            listOfAnswers = (listOfAnswers[6:len(listOfAnswers)-1])


            # Making a List of Answer
            possible_ans=['A','B','C','D']
            for ans in range(0,len(listOfAnswers)):
                if(listOfAnswers[ans].isspace()):
                    continue
                toInsert = str(listOfAnswers[ans][0:6]).rsplit()[-1]
                if (toInsert == 'A' or toInsert == 'B' or toInsert == 'C' or toInsert == 'D'):
                    CORRECT_MCQ_ANSWERS.append(toInsert)

            for ans in range(0, len(listOfAnswers)):
                if (listOfAnswers[ans].isspace() or len(listOfAnswers[ans])<7):
                    continue

                toInsert = str(listOfAnswers[ans]).rsplit()[-1]
                if(toInsert=='A' or toInsert=='B' or toInsert=='C' or toInsert=='D'):
                    CORRECT_MCQ_ANSWERS.append(toInsert)

            return CORRECT_MCQ_ANSWERS
            # print(len(CORRECT_MCQ_ANSWERS))
    else:
        # For Greater than 2016
        PATH = str(question_pdf_path).replace("qp", "ms")
        CORRECT_MCQ_ANSWERS = []
        eachPageAnswer = []
        possible_ans = ['A', 'B', 'C', 'D']
        with pdfplumber.open(PATH) as pdf:
            totalPage = len(pdf.pages)
            for i in range(1,totalPage):
                page_all_texts = (pdf.pages[i].extract_text())
                listOfAnswers = page_all_texts.splitlines()
                # Cutting Unnecessary Values
                listOfAnswers = listOfAnswers[4:len(listOfAnswers)-2]
                # print(listOfAnswers)
                for ans in listOfAnswers:
                    temp_ans = ans[0:6].strip()
                    if(temp_ans.__contains__('A') or temp_ans.__contains__('B') or temp_ans.__contains__('C') or temp_ans.__contains__('D')):
                        # print("Valid : ",temp_ans[-1])
                        eachPageAnswer.append(temp_ans[-1])

                CORRECT_MCQ_ANSWERS+=eachPageAnswer
                eachPageAnswer=[]

        return CORRECT_MCQ_ANSWERS


print(getAnswer('/Users/akifislam/Desktop/QuestionReader/AS  Biology (9700)/2013/9700_w13_ms_11.pdf'))
