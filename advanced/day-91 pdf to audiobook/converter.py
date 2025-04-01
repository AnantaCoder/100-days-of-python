from pdfminer.high_level import extract_text
import re
import unicodedata

def pdf_to_text(pdf_path):
    """Extract text from a PDF file using pdfminer.six."""
    try:
        text = extract_text(pdf_path)  
        text = clean_text(text)        
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

def clean_text(text):
    """Clean and normalize text for TTS."""
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('-\n', '')
    text = ''.join(c for c in text if c.isprintable())
    words = text.split()
    cleaned_words = []
    buffer = []
    for word in words:
        if len(word) == 1:
            buffer.append(word)
        else:
            if len(buffer) >= 3:  
                combined = ''.join(buffer)
                cleaned_words.append(combined)
            else:
                cleaned_words.extend(buffer) 
            buffer = []
            cleaned_words.append(word)
    if len(buffer) >= 3:
        combined = ''.join(buffer)
        cleaned_words.append(combined)
    else:
        cleaned_words.extend(buffer)
    return ' '.join(cleaned_words)