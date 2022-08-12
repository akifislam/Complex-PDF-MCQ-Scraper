PDF_PATH = '/Users/akifislam/Desktop/QuestionReader/AS  Biology (9700)/2018/9700_s18_qp_13.pdf'
import fitz
doc = fitz.open(PDF_PATH)
# print(doc.page_count) #Counting Total Page
# print(doc.load_page(12)) #Loading a page
print(doc.get_toc(2))
page = doc.load_page(10)
pix = page.get_pixmap()
print(pix)
pix.save("page-%i.png" % page.number)
text = page.get_text()
print(text) #Best Extractor EVER :O !