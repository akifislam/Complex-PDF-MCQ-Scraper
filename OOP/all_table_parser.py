import pdfplumber

def getAnswerTableData(PDF_PATH,PAGE_NUMBER):
    ALL_TABLE_DATA = []
    with pdfplumber.open(PDF_PATH) as pdf:
        # print(pdf.pages[PAGE_NUMBER].extract_tables())
        ALL_TABLE_DATA.append(pdf.pages[PAGE_NUMBER].extract_tables())
    # if(len(ALL_TABLE_DATA[0])!=len(OPTIONS_COLUMN_I_J_K_L)):
    #         # print("Q TABLE FOUND")
    # print("For Page " + str(PAGE_NUMBER) + "ALL Table Data : \n " + str(ALL_TABLE_DATA))
    # print()
    # print()
    print("Returning ALL TABLES\n",ALL_TABLE_DATA)
    return ALL_TABLE_DATA