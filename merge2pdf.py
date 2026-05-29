#!/usr/bin/env python
from PIL import Image
from pypdf import PdfReader, PdfWriter
import os
import tempfile

def append_pdf(writer, filename):
    with open(filename, "rb") as f:
        writer.append(f)

def merge_to_single_pdf(input_files, output_pdf):
    writer = PdfWriter()
    for file in input_files:
        ext = os.path.splitext(file)[1].lower()
        # --- image files ---
        if ext in [".jpg", ".jpeg", ".png"]:
            img = Image.open(file)
            if img.mode != "RGB":
                img = img.convert("RGB")
            # save as a temporal PDF and process it.
            with tempfile.NamedTemporaryFile(delete_on_close=False, suffix=".pdf") as fp:
                img.save(fp.name)
                # append the temporal file to output.
                append_pdf(writer, fp.name)
        # --- PDF files ---
        elif ext == ".pdf":
            append_pdf(writer, file)
        # --- unknown files ---
        else:
            print(f"Unknown file type: {file}")
    # At the end, write to the file.
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"merged: {output_pdf}")

if __name__=="__main__":
    import argparse
    default_output = f"{os.path.expanduser("~")}{os.sep}Downloads{os.sep}output.pdf"
    parser = argparse.ArgumentParser(
            description='Convert a list of files into a single PDF')
    parser.add_argument('file', nargs='+',
            help='input file(s) for PDF conversion (JPEG, PNG or PDF)')
    parser.add_argument('-o', '--output', default=default_output,
            help=f"the output file. default value is '{default_output}'")
    args = parser.parse_args()
    merge_to_single_pdf(sorted(args.file), args.output)
