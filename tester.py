import pdfplumber
import time
PDF_PATH = '/Users/akifislam/PycharmProjects/PlumberTest/Resources/AS  Biology (9700)/2011/9700_s11_qp_11.pdf'
PAGE_NUMBER = 8
# For Input in Excels
SL_COLUMN_A = []
QUES_TEXT_COLUMN_B = []


count = 20 #Start of Page Count
with pdfplumber.open(PDF_PATH) as pdf:
  cur_page = pdf.pages[PAGE_NUMBER].extract_text().splitlines()
  for line in cur_page:
    print(line)

