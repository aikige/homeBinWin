#!/usr/bin/env python
from pypdf import PdfReader, PdfWriter

def extract_pages(input_pdf_path, output_pdf_path, pages_to_extract):
    """
    PDFから指定したページだけを抜き出して新しいPDFを作成する関数。

    :param input_pdf_path: 元のPDFファイルパス
    :param output_pdf_path: 抽出後の新しいPDFファイルパス
    :param pages_to_extract: 抜き出すページ番号のリスト（1始まり）
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # ページ番号は0始まりなので調整
    for page_num in pages_to_extract:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
        else:
            print(f"警告: ページ番号 {page_num} は範囲外です。")

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"{len(pages_to_extract)}ページを抽出し、{output_pdf_path} に保存しました。")

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='A simple program which creates PDF subset')
    parser.add_argument('input_file', help='The input file to be cropped')
    parser.add_argument('output_file', help='The output file which stores cropped PDF')
    parser.add_argument('pages_to_extract', help='comma separated number list of pages')
    args = parser.parse_args()
    pages = map(int,args.pages_to_extract.split(','))
    extract_pages(args.input_file, args.output_file, pages)
