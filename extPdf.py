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
    pages = []  # List of pages, integer type.

    # Create list of pages.
    for p in pages_to_extract:
        if '-' in p:
            [start, end] = map(int, p.split('-'))
            pages += list(range(start, end + 1))
        else:
            pages.append(int(p))

    # Adjust page number since array `pages` is zero-based indexing.
    for page_num in pages:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
        else:
            print(f"Warning: page number {page_num} is out of range.")

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Extracted {len(pages)} pages, and stored to {output_pdf_path}.")

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='A simple program which creates PDF subset')
    parser.add_argument('input_file', help='The input file to be cropped')
    parser.add_argument('output_file', help='The output file which stores cropped PDF')
    parser.add_argument('page', nargs='+', help='page (e.g. 2) or range (e.g. 1-5) of pages to be extracted')
    args = parser.parse_args()
    extract_pages(args.input_file, args.output_file, args.page)
