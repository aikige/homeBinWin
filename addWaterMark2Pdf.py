#!/usr/bin/env python
import pikepdf
from pikepdf import Encryption, Permissions

def add_watermark4(input_pdf, watermark_pdf, output_pdf, owner_password):
    # This version works best.
    with pikepdf.Pdf.open(input_pdf) as pdf:
        wm = pikepdf.Pdf.open(watermark_pdf)
        wm_page = wm.pages[0]
        for page in pdf.pages:
            page.add_overlay(wm_page)
        if owner_password:
            pdf.save(
                output_pdf,
                encryption=Encryption(
                    owner=owner_password,   # 管理者パスワード
                    R=4,                      # 暗号化バージョン（通常は4 or 6）
                    allow=Permissions(
                        accessibility=True,   # これだけは True 推奨（アクセシビリティ）
                        extract=False,        # テキスト抽出禁止
                        modify_annotation=False,
                        modify_form=False,
                        modify_other=False,   # ← 変更禁止（重要）
                        print_lowres=False,
                        print_highres=False
                    )
                )
            )
        else:
            pdf.save(output_pdf)
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
    print(f"Protect PDF: {output_pdf}")
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
    args = parser.parse_args()
    add_watermark4(args.input, args.watermark, args.output, args.owner_password)
