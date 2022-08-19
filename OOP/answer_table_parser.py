import pdfplumber
import csv
import answerScrapper as ANSWER_SCRAPPER
from OOP.question_text_parser import collectQuestions
import glob
import time

def getAnswerTableLocation(OPTIONS_COLUMN_I_J_K_L):
    HAS_ANY_ANSWER_TABLE = []
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

    return HAS_ANY_ANSWER_TABLE
    # print("For Page " + str(PAGE_NUMBER) + "Table Location\n" + str(HAS_ANY_ANSWER_TABLE))
    # print()

