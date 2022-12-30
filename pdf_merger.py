from PyPDF2 import PdfMerger
import sys, os

merger = PdfMerger()

if len(sys.argv) < 3:
    sys.exit("usage: python pdf_merger.py [NEW_FILE] [INPUT_FILES]")

files = []
msg = "\nMerging: \n"
for i in range(2, len(sys.argv)):
    files.append("/Users/Adiman17/Downloads/" + sys.argv[i])
    msg += sys.argv[i] + " \n"
print(msg + " ...")

for file in files:
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write(sys.argv[1])
print("Done merging into: " + sys.argv[1] + ".\n")
