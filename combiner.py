# Import the necessary libraries
import PyPDF2
import sys

# This code combines PDF files

# Function to combine PDFs
def combine_pdfs(output_path, *input_paths):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Loop through each input path
    for path in input_paths:
        # Create a PDF reader object for the current path
        pdf_reader = PyPDF2.PdfReader(path)
        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the current page
            page = pdf_reader.pages[page_num]
            # Add the current page to the writer object
            pdf_writer.add_page(page)
    
    # Open the output file in write-binary mode
    with open(output_path, 'wb') as out:
        # Write the combined PDFs to the output file
        pdf_writer.write(out)

# If this script is run directly (not imported as a module)
if __name__ == "__main__":
    # Get the output path from the command line arguments
    output_path = sys.argv[1]
    # Get the input paths from the command line arguments
    input_paths = sys.argv[2:]
    # Call the function to combine the PDFs
    combine_pdfs(output_path, *input_paths)