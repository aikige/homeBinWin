#!/usr/bin/env python
from PIL import Image
from pypdf import PdfReader, PdfWriter
import os
import tempfile

def merge_to_single_pdf(input_files, output_pdf):
    writer = PdfWriter()

    for file in input_files:
        ext = os.path.splitext(file)[1].lower()

        # --- 画像ファイルの場合 ---
        if ext in [".jpg", ".jpeg", ".png"]:
            img = Image.open(file)
            if img.mode != "RGB":
                img = img.convert("RGB")

            # 一時PDFとして保存し、それを処理
            with tempfile.NamedTemporaryFile(delete_on_close=False, suffix=".pdf") as fp:
                img.save(fp.name)
                # PDFとして読み込み
                with open(fp.name, "rb") as f:
                    reader = PdfReader(f)
                    for page in reader.pages:
                        writer.add_page(page)
            
        # --- PDFファイルの場合 ---
        elif ext == ".pdf":
            with open(file, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    writer.add_page(page)

        else:
            print(f"未対応ファイル形式: {file}")

    # 出力
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"merged: {output_pdf}")

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(
            description='Convert a list of files into a single PDF')
    parser.add_argument('file', nargs='+',
            help='input file(s) for PDF conversion (JPEG, PNG or PDF)')
    parser.add_argument('-o', '--output', default='output.pdf',
            help='the output file. default value is "output.pdf"')
    args = parser.parse_args()
    merge_to_single_pdf(args.file, args.output)
