
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
import pyPdf

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace    

    content = " ".join(content.replace("\xa0", " ").strip().split())

    text_file = open("Output.txt", "w")
    text_file.write(content)
    text_file.close()
    return content

print getPDFContent("test.pdf")
