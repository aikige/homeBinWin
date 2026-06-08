#!/usr/bin/env python
import sys
from pypdf import PdfReader, PdfWriter

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    # Read input and watermark PDF.
    reader = PdfReader(input_pdf)
    watermark_reader = PdfReader(watermark_pdf)
    writer = PdfWriter()
    # Assumes watermark is in 1st page.
    watermark_page = watermark_reader.pages[0]
    # Merge watermark for all pages.
    for page_number, page in enumerate(reader.pages):
        # Resize watermark.
        watermark_page.scale_to(width=page.mediabox.width, height=page.mediabox.height)
        # Merge page.
        page.merge_page(watermark_page)
        # Add to output.
        writer.add_page(page)
    # Save output to the file.
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Watermarked PDF saved as: {output_pdf}")

if __name__ == "__main__":
    import argparse
    import os
    default_output = f"{os.path.expanduser("~")}{os.sep}Downloads{os.sep}output.pdf"
    parser = argparse.ArgumentParser(
            description='Add watermark to a PDF')
    parser.add_argument('input',
            help='input PDF file to add a watermark')
    parser.add_argument('-w', '--watermark', default="watermark.pdf",
            help=f"the PDF file which includes watermark image. default value is 'watermark.pdf'")
    parser.add_argument('-o', '--output', default=default_output,
            help=f"the output filename. default value is '{default_output}'")
    args = parser.parse_args()

    add_watermark(args.input, args.watermark, args.output)
