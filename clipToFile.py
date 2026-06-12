#!/usr/bin/env python
import pyperclip
import base64
import io
from PIL import Image, ImageGrab
import sys

def get_clipboard_content():
    """Retrieves image or text content from the clipboard."""
    try:
        # Try getting image from clipboard
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            return "image", img
    except Exception:
        pass # Fallback to text if image grab fails or is not an image

    # Try getting text from clipboard
    text = pyperclip.paste()
    if text:
        return "text", text
    
    return None, None

def save_as_file(content_type, content, basename):
    """Converts content (image or text) into a data URL."""
    if content_type == "image":
        filename = f"{basename}.png"
        with open(filename, "wb") as f:
            content.save(f)
            return filename
    elif content_type == "text":
        filename = f"{basename}.txt"
        with open(filename, "w") as f:
            f.write(content)
            return filename
    return ""

if __name__ == "__main__":
    import argparse
    import os
    default_output = f"{os.path.expanduser("~")}{os.sep}Downloads{os.sep}clip"
    parser = argparse.ArgumentParser(
            description='Save clipbard content into a file (PNG or TXT)')
    parser.add_argument('-o', '--output-basename', default=default_output,
            help=f"change output basename. default value is '{default_output}'")
    args = parser.parse_args()

    content_type, content = get_clipboard_content()
    if content:
        filename = save_as_file(content_type, content, args.output_basename)
        print(f"stored {content_type} content to '{filename}'")
    else:
        print("Clipboard is empty or contains an unsupported format.")
