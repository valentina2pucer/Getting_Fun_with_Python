#the inputs are PDFs that you want to merge in one PDF file

import PyPDF2
import sys

inputs=sys.argv[1:]#vse PDF-je, ki jih podamo

def pdf_combiner(pdf_list):
	merger=PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

#da požene funckijo s temi argumenti
pdf_combiner(inputs)