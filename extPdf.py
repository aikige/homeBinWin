#!/usr/bin/env python
from pypdf import PdfReader, PdfWriter

def extract_pages(input_pdf_path, output_pdf_path, pages_to_extract):
    """
    Function to extract specified page from a PDF and create new one.

    :param input_pdf_path: Path of the original PDF file.
    :param output_pdf_path: Path of the new PDF file.
    :param pages_to_extract: List of pages to be extracted (one-based indexing).
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Adjust page number since array `pages` is zero-based indexing.
    for page_num in pages_to_extract:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
        else:
            print(f"Warning: page number {page_num} is out of range.")

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Extracted {len(pages_to_extract)} pages, and stored to {output_pdf_path}.")

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='A simple program which creates PDF subset')
    parser.add_argument('input_file', help='The input file to be cropped')
    parser.add_argument('output_file', help='The output file which stores cropped PDF')
    parser.add_argument('pages_to_extract', help='comma separated number list of pages')
    args = parser.parse_args()
    pages = map(int,args.pages_to_extract.split(','))
    extract_pages(args.input_file, args.output_file, pages)
