#!/usr/bin/env python
from pypdf import PdfReader, PdfWriter
import os

def split_pages(input_pdf_path):
    """
    Function to split a PDF into single-page files

    :param input_pdf_path: Path of the original PDF file.
    """
    reader = PdfReader(input_pdf_path)
    file_name, _ = os.path.splitext(input_pdf_path)

    for n in range(len(reader.pages)):
        writer = PdfWriter()
        page_num = n + 1;
        output_filename = f"{file_name}_p{page_num}.pdf"
        print(f"{output_filename}")
        writer.add_page(reader.pages[n])
        writer.write(output_filename)
        writer.close()

    print("Extracted.")

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(
            description='A simple program which splits a PDF')
    parser.add_argument('input',
            help='The input file to be broken down')
    args = parser.parse_args()

    split_pages(args.input)
