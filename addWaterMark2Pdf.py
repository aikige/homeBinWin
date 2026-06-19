#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG)

import sys

import pikepdf

from copy import deepcopy
from pypdf.constants import UserAccessPermissions

from pypdf import PdfReader, PdfWriter, Transformation

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from io import BytesIO

def add_watermark4(input_pdf, watermark_pdf, output_pdf, owner_password=None):
    # This version works best.
    pdf = pikepdf.Pdf.open(input_pdf)
    wm = pikepdf.Pdf.open(watermark_pdf)
    wm_page = wm.pages[0]
    for page in pdf.pages:
        page.add_overlay(wm_page)
    pdf.save(output_pdf)
    print(f"Watermarked PDF saved as: {output_pdf}")

def create_svg_overlay(svg_file, page_width, page_height, scale=1.0):
    """
    SVGを読み込んで、指定サイズのPDFオーバーレイを生成
    """
    drawing = svg2rlg(svg_file)
    # SVGサイズ取得
    dw = drawing.width
    dh = drawing.height
    # スケーリング（ページに合わせる）
    scale = min(page_width / dw, page_height / dh) * scale
    # 中央配置
    tx = (page_width - dw * scale) / 2
    ty = (page_height - dh * scale) / 2
    # メモリ上PDF生成
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))
    c.saveState()
    c.translate(tx, ty)
    c.scale(scale, scale)
    # SVG描画
    renderPDF.draw(drawing, c, 0, 0)
    c.restoreState()
    c.save()
    packet.seek(0)
    return PdfReader(packet)

def add_watermark3(input_pdf, svg_file, output_pdf, owner_password=None):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        pw = float(page.mediabox.width)
        ph = float(page.mediabox.height)
        # SVG → overlay PDF生成
        overlay_pdf = create_svg_overlay(svg_file, pw, ph)
        overlay_page = overlay_pdf.pages[0]
        # 合成（前面）
        page.merge_page(overlay_page)
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Saved: {output_pdf}")

def add_watermark2(input_pdf, watermark_pdf, output_pdf, owner_password=None):
    # Read input and watermark PDF.
    reader = PdfReader(input_pdf, strict=False)
    watermark_reader = PdfReader(watermark_pdf, strict=False)
    writer = PdfWriter(strict=False)
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
    # When owner_password is specified, disable modification by encryption.
    if (owner_password):
        user_password = ""
        flag = (UserAccessPermissions.PRINT |
                UserAccessPermissions.EXTRACT |
                UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS)
        writer.encrypt(user_password, owner_password, permissions_flag=flag)
    # Save output to the file.
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Watermarked PDF saved as: {output_pdf}")

def add_watermark(input_pdf, watermark_pdf, output_pdf, owner_password=None):
    # Read input and watermark PDF.
    reader = PdfReader(input_pdf)
    watermark_reader = PdfReader(watermark_pdf)
    writer = PdfWriter()
    # Assumes watermark is in 1st page.
    watermark_page = watermark_reader.pages[0]
    # Merge watermark for all pages.
    for page in reader.pages:
        # Resize watermark.
        watermark_page.scale_to(width=page.mediabox.width, height=page.mediabox.height)
        # Merge page.
        page.merge_page(watermark_page)
        # Add to output.
        writer.add_page(page)
    # When owner_password is specified, disable modification by encryption.
    if (owner_password):
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
    args = parser.parse_args()
    add_watermark5(args.input, args.watermark, args.output, args.owner_password)
