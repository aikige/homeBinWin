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

def save_as_file(content_type, content):
    """Converts content (image or text) into a data URL."""
    if content_type == "image":
        filename = "clip.png"
        with open(filename, "wb") as f:
            content.save(f)
            return filename
    elif content_type == "text":
        filename = "clip.txt"
        with open(filename, "w") as f:
            f.write(content)
            return filename
    return ""

if __name__ == "__main__":
    content_type, content = get_clipboard_content()

    if content:
        filename = save_as_file(content_type, content)
        print(f"stored {content_type} content to '{filename}'")
    else:
        print("Clipboard is empty or contains an unsupported format.")
