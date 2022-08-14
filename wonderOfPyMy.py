PDF_PATH = '/Users/akifislam/Desktop/QuestionReader/AS  Biology (9700)/2011/01.QUES_9700_w11_qp_13.pdf'
import fitz
doc = fitz.open(PDF_PATH)
# print(doc.page_count) #Counting Total Page
# print(doc.load_page(12)) #Loading a page
# print(doc.get_toc(1))
page = doc.load_page(3)
pix = page.get_pixmap()
# print(pix)
pix.save("page-%i.png" % page.number)
text = page.get_text()
print(text) #Best Extractor EVER :O !