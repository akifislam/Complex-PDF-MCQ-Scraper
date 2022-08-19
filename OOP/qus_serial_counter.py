import pdfplumber

def countSerial(PDF_PATH,PAGE_NUMBER,initialCount):
    SL_COLUMN_A = []
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

        print("For Page " + str(PAGE_NUMBER) + "\tQuestion Serial : " + str(SL_COLUMN_A)+"\t",end="| ")
    return SL_COLUMN_A