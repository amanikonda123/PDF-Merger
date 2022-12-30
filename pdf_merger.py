import PyPDF2, sys, os

merger = PyPDF2.PdfFleMerger()

if len(sys.argv) < 2:
    sys.exit("usage: python pdf_merger.py [NEW_FILE] [MERGED_FILES]")

files = []
for i in range(2, len(sys.argv)):
    files.append("/Users/Adiman17/Downloads/" + sys.argv[i])

for file in files:
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write(sys.argv[1])