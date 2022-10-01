import pdfplumber


def collectQuestions(PDF_PATH,PAGE_NUMBER,SL_COLUMN_A):
    QUES_TEXT_COLUMN_B = []
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

    print("For Page " + str(PAGE_NUMBER) +"Questions are\n" +str(QUES_TEXT_COLUMN_B))
    return QUES_TEXT_COLUMN_B


