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

def convert_to_data_url(content_type, content):
    """Converts content (image or text) into a data URL."""
    if content_type == "image":
        buffered = io.BytesIO()
        # Ensure image is in a format suitable for web (e.g., PNG, JPEG)
        # We save it as PNG for simplicity, as it supports transparency
        content.save(buffered, format="PNG") 
        img_str = base64.b64encode(buffered.getvalue())
        return f"data:image/png;base64,{img_str.decode('utf-8')}"
    elif content_type == "text":
        encoded_text = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        # Standard text data URLs can just be URL-encoded, but base64 is often safer for complex text
        # A simple text data URL:
        return f"data:text/plain;charset=utf-8,{pyperclip.quote(content)}" 
        # A base64 text data URL:
        # return f"data:text/plain;base64,{encoded_text}"
    else:
        return None

if __name__ == "__main__":
    content_type, content = get_clipboard_content()

    if content:
        data_url = convert_to_data_url(content_type, content)
        print(f"Data URL generated for {content_type} content:")
        print(data_url)
        # Optionally, copy the data URL back to the clipboard
        pyperclip.copy(data_url)
        print("\nData URL copied to clipboard.")
    else:
        print("Clipboard is empty or contains an unsupported format.")
