#!/usr/bin/env python
from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_pdf_path):
    """
    Merge PDF files into one file.

    :param pdf_list: list of PDF file path to be merged.
    :param output_pdf_path: path of output PDF file.
    """
    writer = PdfWriter()

    for pdf_path in pdf_list:
        with open(pdf_path, "rb") as f:
            writer.append(f)

    with open(output_pdf_path, "wb") as f:
        writer.write(f)

    print(f"Merged {len(pdf_list)} files into {output_pdf_path}.")

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(
            description='A simple program which merges PDF into one file')
    parser.add_argument('input', nargs='+',
            help='The input file to be cropped. Please specify 2 or more files.')
    parser.add_argument('-o', '--output', default='output.pdf',
            help='The output file. Default value is "output.pdf"')
    args = parser.parse_args()

    if len(args.input) < 2:
        parser.print_help()
    else:
        merge_pdfs(args.input, args.output)
