from flask import Flask, request, render_template
from converter import pdf_to_text
from extractor import generate_speech
import os
import base64
import asyncio

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    
    if request.method == "POST":
        if "file" not in request.files:
            return render_template('index.html', error="No file part")
        
        pdf_file = request.files["file"]
        if pdf_file.filename == '':
            return render_template('index.html', error="No file selected")
        
        if not pdf_file.filename.lower().endswith('.pdf'):
            return render_template('index.html', error="Please upload a PDF file")
        
        pdf_path = 'temp.pdf'
        audio_path = None
        
        try:
            pdf_file.save(pdf_path)
            
            extracted_text = pdf_to_text(pdf_path)
            if not extracted_text:
                return render_template('index.html', error="Failed to extract text from PDF")
            
            audio_path = asyncio.run(generate_speech(extracted_text))
            if not audio_path or not os.path.exists(audio_path):
                return render_template('index.html', error="Failed to generate speech")
            
            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")
            
            return render_template('index.html', speech=encoded_audio)
        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")
        finally:
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)