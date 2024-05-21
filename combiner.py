# -*- coding: utf-8 -*-
import PyPDF2
import sys

#irgendwelche Beispieländerungen, um zu gucken, ob das alles funzt 

def combine_pdfs(output_path, *input_paths):
    pdf_writer = PyPDF2.PdfWriter()
    
    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

if __name__ == "__main__":
    output_path = sys.argv[1]
    input_paths = sys.argv[2:]
    combine_pdfs(output_path, *input_paths)

