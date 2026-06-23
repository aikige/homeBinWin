#!/usr/bin/env python
import pikepdf
from pikepdf import Encryption, Permissions

# Create a pikepdf.Encryption object to handle encryption.
def create_pike_encryption(owner_password):
    if owner_password:
        return Encryption(
                owner=owner_password,     # Mandatory to control access.
                allow=Permissions(
                    accessibility=True,   # This should be True
                    extract=False,        # Disable extract texts
                    modify_annotation=False,
                    modify_form=False,
                    modify_other=False,   # Important to disable modify
                    print_lowres=False,
                    print_highres=False
                )
            )
    else:
        return None

# Use pikepdf.JobBuilder for faster processing.
# Note: the `repeat` parameter in `add_overlay` specifies which page-range
#       in `watermark_pdf` is reused for the overlay.
#       Ref: https://qpdf.readthedocs.io/en/stable/cli.html#page-ranges
def add_watermark5(input_pdf, watermark_pdf, output_pdf, owner_password):
    pikepdf.JobBuilder()\
            .input(input_pdf)\
            .add_overlay(watermark_pdf, repeat='1')\
            .encrypt(create_pike_encryption(owner_password))\
            .output(output_pdf)\
            .run()
    print(f"Watermarked PDF saved as: {output_pdf}")

# Use pikepdf for better processing.
# This version may work better when multiple page sizes are used in one document.
def add_watermark4(input_pdf, watermark_pdf, output_pdf, owner_password):
    with pikepdf.Pdf.open(input_pdf) as pdf:
        with pikepdf.Pdf.open(watermark_pdf) as wm:
            wm_page = wm.pages[0]
            for page in pdf.pages:
                page.add_overlay(wm_page)
            pdf.save(output_pdf, encryption=create_pike_encryption(owner_password))
            print(f"Watermarked PDF saved as: {output_pdf}")

from copy import deepcopy
from pypdf.constants import UserAccessPermissions
from pypdf import PdfReader, PdfWriter, Transformation

def add_watermark2(input_pdf, watermark_pdf, output_pdf, owner_password):
    # Read input and watermark PDF.
    reader = PdfReader(input_pdf, strict=False)
    watermark_reader = PdfReader(watermark_pdf, strict=False)
    writer = PdfWriter()
    # Assumes watermark is in 1st page.
    watermark_page = watermark_reader.pages[0]
    # Merge watermark for all pages.
    for page in reader.pages:
        # Duplicate object to avoid confliction of references.
        watermark_tmp = deepcopy(watermark_page)
        # Retrieve page sizes.
        pw = float(page.mediabox.width)
        ph = float(page.mediabox.height)
        ww = float(watermark_tmp.mediabox.width)
        wh = float(watermark_tmp.mediabox.height)
        # Identify scale to fit page.
        scale = min(pw / ww, ph / wh)
        # Offset to center image.
        tx = (pw - ww * scale) / 2
        ty = (ph - wh * scale) / 2
        # Create transformation object.
        transformation = Transformation().scale(scale).translate(tx, ty)
        # Merge with scales.
        page.merge_transformed_page(watermark_tmp, transformation)
        # Add to output.
        writer.add_page(page)
    if owner_password:
        user_password = ""
        flag = (UserAccessPermissions.PRINT |
                UserAccessPermissions.EXTRACT |
                UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS)
        writer.encrypt(user_password, owner_password, permissions_flag=flag)
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
    parser.add_argument('-p', '--owner-password', default=None,
            help="if specified, protect the output PDF from editing with a password")
    parser.add_argument('-v', '--algorithm-version', type=int, choices=[2,4,5], default=5,
            help="specify algorithm version. default is 5")
    args = parser.parse_args()

    if args.algorithm_version == 2:
        add_watermark2(args.input, args.watermark, args.output, args.owner_password)
    elif args.algorithm_version == 4:
        add_watermark4(args.input, args.watermark, args.output, args.owner_password)
    else:
        add_watermark5(args.input, args.watermark, args.output, args.owner_password)
