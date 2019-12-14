import PyPDF2
pdfFile = open('JaiminResume.pdf','rb')
readFile = PyPDF2.PdfFileReader(pdfFile)
no = readFile.numPages
page = readFile.getPage(no-1)
text = page.extractText()

file1 = open(r"E:\\jaimin\\Python\\Resume.txt","a")
file1.writelines(text)
file1.close()